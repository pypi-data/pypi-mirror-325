

def test_plugin_registration(test_app):

    # Get plugin from app
    plugins = test_app.plugins(name="net.bytebutcher.baukasten.test.singleton_plugin", type="test")
    assert len(plugins) == 1

    plugin_instance = plugins[0]
    assert plugin_instance.metadata.name == "net.bytebutcher.baukasten.test.singleton_plugin"
    assert plugin_instance.metadata.type == "test"
    assert plugin_instance.metadata.version == "v1"


def test_plugin_initialization_behavior(test_app):
    # Test singleton behavior


    # Get plugin multiple times and verify singleton behavior
    plugin1 = test_app.plugin(name="net.bytebutcher.baukasten.test.singleton_plugin", type="test")
    plugin2 = test_app.plugin(name="net.bytebutcher.baukasten.test.singleton_plugin", type="test")

    plugin1.increment()
    assert plugin2.counter == 1  # Should share state