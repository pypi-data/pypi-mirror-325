

class Yapsy:

    def __init__(self):
        self._baukasten = Baukasten()

    def setPluginPlaces(self, plugin_places):
        for plugin_place in plugin_places:
            self._baukasten.plugins.register(plugin_place)

    def collectPlugins(self):
        """ Load all plugins. """
        self.locatePlugins()
        self.loadPlugins()

    def locatePlugins(self):
        self._baukasten.plugins.update()

    def loadPlugins(self, pre_callback = None, init_callback = None, post_callback = None):
        for plugin in self._baukasten.plugins:
            if pre_callback:
                pre_callback(plugin)
            if init_callback:
                plugin = init_callback(plugin)
            if post_callback:
                post_callback(plugin)

    def getAllPlugins(self) -> List:
        return []



def test_load_directory(test_data_path):
    yapsy = Yapsy()
    yapsy.setPluginPlaces(test_data_path)
    yapsy.collectPlugins()
    for plugin_info in yapsy.getAllPlugins():
        plugin_info.plugin_object.doSomething()