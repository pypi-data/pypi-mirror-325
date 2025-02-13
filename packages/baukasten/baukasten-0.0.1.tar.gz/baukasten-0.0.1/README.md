<p align="center">
   <img src="data/logo/python-baukasten-64.png" width="64" height="64" alt="Logo" style="vertical-align: middle;">
</p>
<h1 align="center" style="margin-top: 0px;">Python Baukasten</h1>


**Python Baukasten** is an easy to use pluggable plugin framework for python. 
It is a result of a long period of comparing numerous python plugin frameworks, identifying their key characteristics
and designing an interface which allows to develop your own plugin manager 
with all the features you need
while providing a sane default 
implementation supporting the following features:

- Import of plugins from entry-points, folders, modules, packages, and classes
- Configurable automatic initialization of plugins
- Filterable custom plugin metadata definition
- Easy to manage persistent plugin manager and plugin configuration
- Dependency-, version- and update-management

## Usage

This section illustrates how to use the default implementation of ```Python Baukasten```.
```
app_dir = os.path.abspath(os.path.dirname(__file__))
context = baukasten.Context(app_dir=app_dir, app_name="my-app")
plugin_manager = baukasten.PluginManager(context)
```

By default the ```PluginManager``` searches for plugins at the following locations:
- app_dir/plugins (e.g. /path/to/application/plugins)
- xdg_data_dir/plugins (e.g. /home/user/.config/app_name/plugins)
- entry-points

Plugins are detected via the ```@plugin``` decorator which can be used on functions, classes, and methods.
It accepts arbitrary arguments which can be used to enrich the plugin with metadata.
```
@plugin(spam="egg", egg="spam")
def my_function():
    return 42

@plugin(egg="spam")
class MyClass:
    pass
    
class OtherClass:
    
    @plugin(spam="egg")
    def my_method(self):
        return 42
```
TODO: derive from yet unknown class (e.g. depends on other plugin)
To retrieve the plugins the ```filter``` method can be used:
```
# Gather all plugins
plugins = plugin_manager.filter()

# Gather plugins filtering on metadata
plugins = plugin_manager.filter(spam="egg")
```

## Advanced Usage

### Configuration

The default implementation of ```Python Baukasten``` supports two types of persistent configurations. The 
plugin manager configuration used for storing settings related how plugins are loaded and processed and plugin 
configuration where individual settings of a plugin can be stored.

### Hooks

When initializing the ```PluginManager``` a list of hooks can be passed:

```
plugin_manager = baukasten.PluginManager(context, hooks=[
    PluginPreLoadHook(lambda plugins: filter(lambda plugin: plugin.__plugin_metadata.get("egg") == "spam", plugins)),
    PluginInitHook(lambda plugin: plugin("parameter-1", "parameter-2", ...))
])
```
