from __future__ import annotations

import contextlib
import copy
import inspect
import sys
import os.path
from types import SimpleNamespace
from typing import List, Callable
from importlib import util as ilu

from baukasten.helpers import classname, is_later_version
from baukasten.logger import get_logger
from baukasten.models import Core, Plugin, PostRegisterPlugin, PluginLifecycle


# Registry containing all registered plugins.
_plugin_registry = {}

# Logger used during plugin registration.
logger = get_logger("plugin_registry")

# Global allow list for plugins - stores absolute paths of files and directories
# Allow list is maintained by plugin directory crawler to enforce controlled plugin loading.
_plugin_registry_allow_list = {}

def allow_plugin(path: str) -> None:
    abs_path = os.path.abspath(path)
    _plugin_registry_allow_list[abs_path] = True

def is_plugin_allowed(path: str) -> bool:
    abs_path = os.path.abspath(path)
    dir_path = os.path.dirname(abs_path)
    return abs_path in _plugin_registry_allow_list or dir_path in _plugin_registry_allow_list

# Allow core-plugins to be loaded automatically.
allow_plugin(os.path.dirname(__file__))

def plugin(**kwargs):
    """ Decorator used in plugin classes for registering plugin class and supplying metadata. """
    required_fields = {'name', 'type', 'version'}

    def decorator_plugin(clazz):
        # Get plugin file path
        plugin_file = inspect.getfile(clazz.__init__)

        if not is_plugin_allowed(plugin_file):
            # Do not allow uncontrolled plugin loading.
            logger.debug(f'Plugin {plugin_file} is not in the allowed list...')
            return

        # TODO: Is this still required?
        # if "unittest" in sys.plugins:
        #    return clazz

        if classname(clazz) in _plugin_registry:
            logger.debug(f'Skipping registration of duplicate plugin "{classname(clazz)}"!')
            return

        # Log decorator arguments
        logger.info(f'Registering "{classname(clazz)}"')
        logger.debug(f'Decorator: {kwargs}')

        # Validate plugin class inherits from Plugin
        if not issubclass(clazz, Plugin):
            raise TypeError(f"{clazz.__name__} must inherit from Plugin")

        # Require that the plugin implements an __init__ method.
        # Note: This is required to locate the plugin location via inspect.getfile(clazz.__init__).
        if '__init__' not in vars(clazz):
            raise Exception(f'Plugin "{classname(clazz)}" does not implement an __init__ method!')

        # Make sure that the decorator uses all required fields.
        if not set(kwargs).issuperset(required_fields):
            missing = required_fields - set(kwargs)
            raise ValueError(f"Missing required plugin fields: {missing}")

        # Make metadata available to plugin class. In order to improve accessibility the dictionary is transformed to
        # a namespace object which allows direct access to the fields.
        metadata = clazz.metadata.__dict__ if hasattr(clazz, 'metadata') and \
                                                            clazz.metadata is not None else kwargs
        logger.debug(f'Metadata: {metadata}')
        clazz.metadata = SimpleNamespace(**{**metadata, **kwargs})

        # Annotate plugin file. Points to the absolute filename of the plugin class.
        clazz.metadata.file = inspect.getfile(clazz.__init__)
        logger.debug(f'File: {clazz.metadata.file}')

        # Annotate that plugin is currently not initialized.
        clazz.metadata.initialized = False

        # Do not add plugin to registry if plugin is marked as disabled.
        if (hasattr(clazz.metadata, 'disabled') and clazz.metadata.disabled) or \
                (hasattr(clazz.metadata, 'enabled') and not clazz.metadata.enabled):
            logger.debug(f'Disabled: True')
            logger.debug(f'Aborted registering plugin "{classname(clazz)}" ...')
            logger.debug(f'Current registry: {list(_plugin_registry.keys())}')
            return clazz

        # Register plugin.
        _plugin_registry[classname(clazz)] = clazz
        logger.debug(f'Successfully registered plugin "{classname(clazz)}" ...')
        logger.debug(f'Current registry: {list(_plugin_registry.keys())}')
        # Return class reference to caller again.
        return clazz

    return decorator_plugin


@contextlib.contextmanager
def spec_from_file(file: str):
    path = os.path.dirname(file)
    was_path_updated = False
    try:
        if path not in sys.path:
            sys.path.insert(0, path)
            was_path_updated = True
        modname = inspect.getmodulename(file)
        spec = ilu.spec_from_file_location(modname, file)
        if spec is None:
            raise ImportError(f'Could not load spec for plugin "{modname}" at: {file}')
        yield spec
    finally:
        if was_path_updated:
            sys.path.remove(path)


class PluginManager(Core):
    """
    PluginManager supporting directory- and decorator-based loading mechanism and dynamic filtering.


    Plugin Directory Structure:

    .
    ├── plugin_a
    │   └── __init__.py
    └── plugin_b
        └── __init__.py

    Plugin Class Structure:

    ```
    @plugin_v1(egg="spam")
    class PluginA:

        def __init__(self):
            pass
    ```
    """

    def __init__(self, app: 'app.Baukasten'):
        """
        Initializes the PluginManager.
        :param app: The application context.
        """
        super().__init__(app)
        self._plugin_filter = PluginFilter(app)

    def _is_plugin_file(self, fname: str) -> bool:
        """
        Checks whether the specified filename is a valid plugin file.
        :param fname: a filename (e.g. "main.py")
        :return: True, if the specified file is a plugin file, otherwise False.
        """
        return fname.endswith('.py')

    def _register_plugin_from_file(self, file: str):
        """
        Loads the plugin from the specified file. Registration of plugin is done automatically via plugin-decorator.
        :param file: file where the plugin is located (e.g. "plugins/plugin_a.py")
        """
        logger.debug(f"Loading plugin from file: {file}")
        try:
            with spec_from_file(file) as spec:
                module = ilu.module_from_spec(spec)
                spec.loader.exec_module(module)
        except Exception as e:
            logger.error(f"Failed to register plugin from {file}: {str(e)}")
            raise

    def _crawl_plugin_directories(self, directories: List[str] = None) -> List[str]:
        """
        Crawls the specified directories and returns a list of files where plugins are suspected to be located
        :param directories: the directories where plugins are located.
        :return: the files where plugins are suspected to be located.
        """
        file_count = 0
        directories = directories if directories else []
        logger.debug(f"Crawling directories: {directories}")
        for directory in directories:
            logger.debug(f"Scanning directory: {directory}")

            if not os.path.exists(directory):
                logger.warning(f"Directory does not exist: {directory}")
                continue

            for path, dirs, file_names in os.walk(directory):
                logger.debug(f"Walking path: {path}")
                logger.debug(f"Found subdirs: {dirs}")
                logger.debug(f"Found files: {file_names}")
                if '__pycache__' in path:
                    # Skip __pycache__ directories which are automatically created when plugins are initialized.
                    logger.debug(f"Skipping __pycache__ directory: {path}")
                    continue

                for file_name in file_names:
                    file = os.path.join(path, file_name)
                    if self._is_plugin_file(file):
                        logger.debug(f"Found plugin file: {file}")
                        allow_plugin(file)
                        file_count += 1
                        yield file
                    else:
                        logger.debug(f"Skipping non-plugin file: {file}")

        logger.debug(f"Found plugin files: {file_count}")

    def _register_plugins(self, directories: List[str] = None):
        """
        Registers plugins within specified directories.
        :param directories: the directories where plugins are located.
        """
        for file in self._crawl_plugin_directories(directories):
            try:
                logger.debug(f'Loading plugin from {file} ...')
                self._register_plugin_from_file(file)
            except Exception as err:
                logger.error(f'Loading plugin from {file} failed!')
                raise err

    def _post_register_plugins(self):
        self_filter = self.filter(type='built-in.plugin-post-register')
        for plugin in self_filter:
            plugin: PostRegisterPlugin
            for _plugin in _plugin_registry.values():
                plugin.run(_plugin)

    def register_plugins(self, plugins_dirs: List[str] = None, clear_cache: bool = True):
        """
        Registers plugins.
        :param plugins_dirs: The directories where plugins are located.
        :param clear_cache: Defines, whether the plugin cache should be cleared before registering the new plugins.
                            If set to False, only new plugins will be added and plugins with the same qualified name
                            will not be updated. There is no force_plugin_update mechanism at the moment.
        """
        logger.debug(f"Starting plugin registration with dirs: {plugins_dirs}")
        if clear_cache:
            self._clear_cache()

        if plugins_dirs:
            self._register_plugins(plugins_dirs)
        self._post_register_plugins()

    def _clear_cache(self):
        """
        Clears the plugin registry while preserving core plugins.

        Core plugins are identified by being located in the same directory as
        the plugin loader. This ensures that critical system plugins  remain
        available after cache clearing.
        """
        app_core_dir = os.path.dirname(inspect.getfile(PluginManager))
        core_plugins = {name: plugin for name, plugin in _plugin_registry.items()
                        if hasattr(plugin.metadata, 'file') and os.path.dirname(plugin.metadata.file) == app_core_dir}
        logger.debug("Clearing plugin registry cache")
        _plugin_registry.clear()
        _plugin_registry.update(core_plugins)

    def filter(self, *args, **kwargs) -> List[Plugin]:
        """
        Filters the registered plugins by supplied filter terms and returns matching plugins.

        Example:

            filter(foo='bar', egg='spam')

        :returns list of plugin containers. Plugins are not initialized. See plugin-decorator for more
                information regarding how the plugin container is constructed.
        """
        return self._plugin_filter.filter(*args, **kwargs)


class PluginInit:

    def __init__(self, plugin, init_callback):
        self._plugin = plugin
        self._init_callback = init_callback

    def is_initialized(self) -> bool:
        return self._plugin.metadata.initialized

    def is_init_callback_provided(self) -> bool:
        return self._init_callback is not None

    def perform_on_initialized_plugin(self):
        raise NotImplementedError()

    def perform_on_uninitialized_plugin(self):
        raise NotImplementedError()

    def perform(self):
        if self.is_initialized():
            return self.perform_on_initialized_plugin()
        else:
            return self.perform_on_uninitialized_plugin()


class ManualPluginInit(PluginInit):

    def perform_on_initialized_plugin(self):
        # if self.is_init_callback_provided():
        #    raise Exception('Illegal arguments! '
        #                    f'Plugin {classname(self._plugin)} is configured to be returned uninitialized '
        #                    f'but an init callback was provided!')
        # Return the copy of the uninitialized plugin class.
        return copy.copy(self._plugin.__class__)

    def perform_on_uninitialized_plugin(self):
        # if self.is_init_callback_provided():
        #    raise Exception('Illegal arguments! '
        #                    f'Plugin {classname(self._plugin)} is configured to be returned uninitialized '
        #                    f'but an init callback was provided!')
        # Returns the uninitialized plugin.
        return copy.copy(self._plugin)


class InstancePluginInit(PluginInit):

    def perform_on_initialized_plugin(self):
        # Returns a new initialized plugin.
        return lambda: self._init_callback(copy.copy(self._plugin.__class__))

    def perform_on_uninitialized_plugin(self):
        # Returns a new initialized plugin.
        return self._init_callback(copy.copy(self._plugin))


class SingletonPluginInit(PluginInit):

    def perform_on_initialized_plugin(self):
        # if self.is_init_callback_provided:
        #    raise Exception('Illegal arguments! '
        #                    f'Plugin {classname(self._plugin)} is configured as singleton and already initialized '
        #                    f'but an init callback was provided!')
        # Returns the already initialized plugin.
        return self._plugin

    def perform_on_uninitialized_plugin(self):
        # Returns the initialized plugin.
        return self._init_callback(self._plugin)


class PluginFilter(Core):

    def __init__(self, app: 'app.Baukasten'):
        super().__init__(app)

    def filter(self, *args, **kwargs):
        logger.debug(f"Filtering plugins (args: {args}, kwargs: {kwargs})")
        plugins = []
        logger.debug(f"Iterating plugins: {list(_plugin_registry.keys())}")
        for plugin in _plugin_registry.values():
            logger.debug(f">> {plugin}: '{plugin.metadata}")
            if not self._does_plugin_matches_filter_terms(plugin, *args, **kwargs):
                # Skip non-matching plugins.
                continue
            plugins.append(self._bootstrap_plugin(plugin))
        return self._post_process(plugins, args, kwargs)

    def _does_plugin_matches_filter_terms(self, plugin: Plugin, *args, **kwargs) -> bool:
        """ Returns whether the plugin matches all the filter terms. """
        metadata = plugin.metadata.__dict__
        for key in args:
            if key not in metadata:
                logger.debug(f"Result: False, arg key '{key}' not found in metadata")
                return False
        for key, value in kwargs.items():
            if key not in metadata:
                logger.debug(f"Result: False, kwarg key '{key}' not found in metadata")
                return False
            if isinstance(metadata[key], list):
                if value not in metadata[key]:
                    logger.debug(f"Result: False, value '{value}' not found in metadata list {metadata[key]}")
                    return False
            else:
                if value != metadata[key]:
                    logger.debug(
                        f"Result: False, value mismatch for '{key}': expected '{value}', got '{metadata[key]}'")
                    return False
        logger.debug(f"Result: True")
        return True

    def _bootstrap_plugin(self, plugin: Plugin) -> Callable:
        """ Returns a callback which initializes the plugin according to the specified plugin_init_behaviour. """
        logger.debug(f'Bootstrapping plugin "{plugin.metadata.name}" with {plugin.__lifecycle__} strategy...')
        logger.debug(f'')
        init_callback = lambda clazz: clazz(self._app)
        plugin = {
            PluginLifecycle.MANUAL: ManualPluginInit,
            PluginLifecycle.INSTANCE: InstancePluginInit,
            PluginLifecycle.SINGLETON: SingletonPluginInit
        }.get(plugin.__lifecycle__)(plugin, init_callback).perform()
        if plugin.__lifecycle__ == PluginLifecycle.SINGLETON:
            plugin.metadata.initialized = True
            _plugin_registry[classname(plugin)] = plugin
        return plugin

    def _post_process(self, plugins: List[Plugin], args, kwargs) -> List[Plugin]:
        """ Some post-processing mechanisms after plugins were loaded. """
        if len(plugins) == 0:
            return plugins

        if kwargs.get('version'):
            self._check_for_deprecated_versions(plugins)

        return plugins

    def _check_for_deprecated_versions(self, plugins: List[Plugin]):
        """
        Checks whether the version of the loaded plugins are deprecated and prints a warning.
        The deprecation check can be turned off via the plugin decorator by adding a "deprecated=False" attribute.
        This may be useful in instances where the old implementations is still required (e.g. parsers).
        """
        for plugin in plugins:
            is_deprecated = hasattr(plugin.metadata, "deprecated") and plugin.metadata.deprecated
            if not hasattr(plugin.metadata, "deprecated") or is_deprecated:
                for _plugin in _plugin_registry.values():
                    if plugin.metadata.name == _plugin.metadata.name and plugin.metadata.type == _plugin.metadata.type:
                        if not is_later_version(plugin.metadata.version, _plugin.metadata.version):
                            logger.warning(f'The version {plugin.metadata.version} of {plugin.metadata.type}/'
                                                 f'{plugin.metadata.name} is deprecated! '
                                                 f'Update the source code to use the latest version of '
                                                 f'{plugin.metadata.type}/{plugin.metadata.name} or set '
                                                 f'"deprecated=False" in the associated plugin decorator in order to '
                                                 f'prevent this warning from appearing.')
                            break
