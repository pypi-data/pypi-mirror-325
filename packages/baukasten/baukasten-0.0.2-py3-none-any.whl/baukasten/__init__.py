import logging
import os
from collections import defaultdict
from configparser import ConfigParser
from typing import List, Callable, Any, TypeVar

from baukasten.config import Config
from baukasten.event_bus import EventBus
from baukasten.helpers import get_class_caller_path
from baukasten.models import Plugin


T = TypeVar('T', bound=Plugin)


class Baukasten:
    """ The main application. """

    def __init__(self):
        """ Initializes the main application. """
        self._path = get_class_caller_path()
        self._config = None
        self._plugin_manager = None
        self._event_bus = None

    @property
    def event_bus(self) -> 'baukasten.event_bus.EventBus':
        if not self._event_bus:
            self._event_bus = EventBus()
        return self._event_bus

    @property
    def config(self) -> Config:
        """ Returns the config. """
        if not self._config:
            self._config = Config(self._path)
        return self._config

    @property
    def plugin_manager(self) -> 'baukasten.registry.PluginManager':
        """ Returns the plugin manager. """
        if not self._plugin_manager:
            from baukasten.registry import PluginManager
            self._plugin_manager = PluginManager(app=self)
            self._plugin_manager.register_plugins(plugins_dirs=self.config.read_list('plugin_manager', 'plugin_dirs'))
        return self._plugin_manager

    def plugins(self, *args, **kwargs) -> List[Plugin]:
        """ Returns the plugins matching the filter terms. """
        return [plugin for plugin in self.plugin_manager.filter(*args, **kwargs)]

    def plugin(self, *args, **kwargs) -> T:
        """ Returns the plugin matching the filter terms. Raises exception when multiple or no plugins are found. """
        plugins = self.plugins(*args, **kwargs)
        if len(plugins) != 1:
            message = os.linesep.join([
                f'Error retrieving plugin matching {args}, {kwargs}!',
                f'Expected 1 plugin, got {len(plugins)}!'
            ])
            raise Exception(message)
        return plugins[0]
