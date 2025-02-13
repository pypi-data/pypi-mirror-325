import inspect
import os
import pathlib
from distutils.version import LooseVersion
from importlib.metadata import version
from typing import List, TypeVar, Union, Type, Dict, Tuple

from baukasten.models import Core, Plugin, Model
from baukasten.logger import get_logger


logger = get_logger('helpers')
T = TypeVar("T")


def get_package_name():
    """Get the package name """
    return __package__ if __package__ else __name__.split('.')[0]


def classname(clazz: Union[Type, object]):
    if hasattr(clazz, '__qualname__'):
        return clazz.__qualname__
    if hasattr(clazz, '__name__'):
        return clazz.__name__
    if hasattr(clazz, '__class__'):
        return classname(clazz.__class__)
    raise Exception(f'Error retrieving class name for {clazz}!')


def get_class_caller_path() -> pathlib.Path:
    """Get directory of the module that called the class"""
    caller_frame = inspect.currentframe().f_back.f_back  # Two frames back: function -> caller
    try:
        caller_module = inspect.getmodule(caller_frame)
        # Get the file path of the calling module and its parent directory
        return pathlib.Path(caller_module.__file__).parent.resolve()
    finally:
        del caller_frame  # Clean up to prevent reference cycles


def latest_version(versions: List[str]) -> str:
    """
    :param versions: a list of versions (e.g. ['latest', 'v1', 'v2.2'])
    Returns the item in a list which has the max version.
    """
    if 'latest' in versions:
        return 'latest'
    try:
        # Removing the leading 'v' from the version strings (e.g. 'v1' -> '1').
        versions_sorted = [v[1:] for v in versions]
        # Sorting versions
        versions_sorted.sort(key=LooseVersion)
        # Returning latest version, reattaching leading 'v' again.
        return 'v' + versions_sorted[-1]
    except Exception:
        raise Exception('Looking up latest version failed! Invalid version strings detected in {versions}!')


def is_later_version(version_1, version_2) -> bool:
    """ Returns whether version_1 is newer then version_2. """
    return latest_version([version_1, version_2]) == version_1


def get_app_version() -> str:
    package_name = get_package_name()
    return version(package_name)


class Runner:

    def __init__(self, callback=None):
        self.callback = callback

    def run(self, *args):
        if self.callback:
            self.callback(*args)


class Command:

    def run(self, *args, **kwargs):
        raise NotImplemented()


class ModelGenerator(Core):

    def __init__(self, app: 'app.Baukasten', name: str, version: str = None, *args, **kwargs):
        super().__init__(app)
        self._name = name
        self._models = self._init_models(name, version, *args, **kwargs)

    def _init_models(self, name: str, version: str, *args, **kwargs) -> List[Tuple[Model, List[str]]]:
        result = []
        for model in self._get_models(name, version, *args, **kwargs):
            result.append((model, self._get_model_fields(model)))
        return result

    def _get_model_fields(self, model: object) -> Dict[str, str]:
        return {field for field in inspect.getfullargspec(model.__init__).args if field != 'self'}

    def _get_models(self, name: str, version: str = None, *args, **kwargs) -> List[Plugin]:
        if version:
            return self._app.plugins(
                name=name, type='built-in.model', version=version, init=lambda plugin: plugin, *args, **kwargs)
        else:
            return self._app.plugins(
                name=name, type='built-in.model', init=lambda plugin: plugin, *args, **kwargs)

    def generate(self, clazz: object) -> List[object]:
        def _getvars():
            if isinstance(clazz, dict):
                return clazz
            elif hasattr(clazz, '__init__'):
                args = inspect.getfullargspec(clazz.__init__).args
                return {arg: getattr(clazz, arg) for arg in args if arg != 'self'}
            else:
                logger.debug(f'{clazz}')
                raise Exception(f'Can not handle {type(clazz)}!')

        clazz_vars = _getvars()
        clazz_fields = clazz_vars.keys()
        for model, model_fields in self._models:
            if clazz_fields == model_fields:
                logger.trace(f'Model {model} is matching the following fields: {", ".join(model_fields)}')
                return model(**clazz_vars).generate()
            model_missing_fields = [clazz_field for clazz_field in clazz_fields if clazz_field not in model_fields]
            logger.trace(f'Model {model} is missing the following fields: {", ".join(model_missing_fields)}')
        logger.debug(f'{self._name}: {clazz}')
        for model, model_fields in self._models:
            logger.debug(f'{model}: {model_fields}')
        raise Exception(f'Error retrieving {self._name} model!')


def comparer(**kwargs):
    def decorator_comparer(clazz):
        def _getarg(name, default=None):
            if hasattr(kwargs, name) and kwargs[name]:
                return kwargs[name]
            else:
                return default

        def _getattr(obj, name):
            value = getattr(obj, name)
            return value if not isinstance(value, list) else os.linesep.join(value)

        def _getfields(obj):
            fields = []
            for field in vars(obj):
                if field != 'self' and field not in exclude_list:
                    fields.append(field)
            return fields

        def _hash(obj):
            return hash((_getattr(field, obj) for field in _getfields(obj)))

        def _eq(obj, other):
            obj_fields = _getfields(obj)
            other_fields = _getfields(other)
            if obj_fields != other_fields:
                return False
            for field in obj_fields:
                if _getattr(obj, field) != _getattr(other, field):
                    return False
            return True

        def _repr(obj, fields, max_length):
            result = f'<{type(obj)}'
            fields = fields or _getfields(obj)
            for field in fields:
                value = _getattr(obj, field)
                if value:
                    result += f' {field}:{value if len(value) <= max_length else hash(value)}'
                else:
                    result += f' {field}:None'
            return result + '>'

        field_list = _getarg('fields', default=[])
        max_length = _getarg('max_length', default=64)
        exclude_list = _getarg('exclude_list', default=[])
        clazz.__hash__ = lambda cls: _hash(cls)
        clazz.__eq__ = lambda cls, other: _eq(cls, other)
        clazz.__repr__ = lambda cls: _repr(cls, field_list, max_length)
        return clazz

    return decorator_comparer
