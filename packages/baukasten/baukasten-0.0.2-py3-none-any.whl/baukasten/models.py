from enum import Enum
from types import SimpleNamespace
from typing import List, Union, Type

from baukasten.logger import get_logger


logger = get_logger('models')


class PluginLifecycle(Enum):
    MANUAL = "manual"  # Manual init, multiple instances allowed
    INSTANCE = "instance"  # Auto init, multiple instances allowed
    SINGLETON = "singleton"  # Auto init, single instance enforced


def classname(clazz: Union[Type, object]):
    if hasattr(clazz, '__qualname__'):
        return clazz.__qualname__
    if hasattr(clazz, '__name__'):
        return clazz.__name__
    if hasattr(clazz, '__class__'):
        return classname(clazz.__class__)
    raise Exception(f'Error retrieving class name for {clazz}!')


def overrides(interface_class):
    """ Decorator used to indicate that a method overrides a method of a parent class. """

    def overrider(method):
        assert (method.__name__ in dir(interface_class))
        return method

    return overrider


class Core:
    """ Core model providing access to the application context and to a individual logger. """

    def __init__(self, app: 'app.Baukasten'):
        self._app = app


class Model:

    def generate(self) -> List['Model']:
        """
        Capability to generate a list of models out of a model. This might be necessary when a field in the current
        model version (e.g. v1) should be expanded to multiple models in the next version (e.g. v2).
        By default, this method returns a list containing only the actual model.

        See subclasses which override this method for more information.
        """
        return [self]


class Plugin(Core):
    """
    A Plugin. Singleton.

    Example:

        @plugin(name='my_plugin', type='some_type', version='v1')
        class MyPlugin(Plugin)

            def __init__(self, app):
                super().__init__(app)

            def do_something(self):
                print('Doing something ...')


        from baukasten.app import App
        App("my_app").plugin(name='my_plugin', type='some_type').do_something()

    """
    __lifecycle__ = PluginLifecycle.SINGLETON
    metadata = SimpleNamespace()

    def __init__(self, app: 'app.Baukasten'):
        """ Initializes the plugin class. """
        super().__init__(app)

    @property
    def config(self):
        plugin_name = classname(self)
        if not self._app.config.has_section(plugin_name):
            self._app.config.add_section(plugin_name)
        return self._app.config[plugin_name]


class ManualPlugin(Plugin):
    __lifecycle__ = PluginLifecycle.MANUAL


class InstancePlugin(Plugin):
    __lifecycle__ = PluginLifecycle.INSTANCE


class SingletonPlugin(Plugin):
    __lifecycle__ = PluginLifecycle.SINGLETON


class Api(SingletonPlugin):
    """ Denotes that the inherited class is an API. """
    pass


class Command(SingletonPlugin):
    """ Denotes that the inherited class is a Tool. """
    pass


class Builder(SingletonPlugin):
    """ Denotes that the inherited class is a Builder. """

    def build(self):
        pass


class Formatter(SingletonPlugin):
    """ Denotes that the inherited class is a formatter. """

    def print(self, clazz, columns, elements):
        raise NotImplemented('This method is not implemented!')


class Parser(InstancePlugin, SingletonPlugin):
    """ Denotes that the inherited class is a parser. """

    def parse_file(self, file: str):
        raise NotImplementedError()

    def parse_files(self, files: List[str]):
        for file in files:
            logger.debug(f'Parser[{self.metadata.name}]: Start parsing {file} ...')
            yield self.parse_file(file)

    def parse(self, files: List[str]):
        return self.parse_files(files)


class PostRegisterPlugin(InstancePlugin, SingletonPlugin):
    """ Denotes that the inherited class is a post-registration plugin. """

    def run(self, clazz):
        raise NotImplemented('This method is not implemented!')
