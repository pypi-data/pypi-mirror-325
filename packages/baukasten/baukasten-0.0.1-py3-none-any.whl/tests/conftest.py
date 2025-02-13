from pathlib import Path

import pytest
import tempfile
import os
from baukasten.__init__ import Baukasten


@pytest.fixture
def temp_dir():
    with tempfile.TemporaryDirectory() as tmpdirname:
        yield tmpdirname


@pytest.fixture
def test_data_path():
    return Path(__file__).parent / "data"


@pytest.fixture
def test_data_plugins_path(test_data_path):
    return test_data_path / "plugins"


@pytest.fixture
def test_app(test_data_path):
    app = Baukasten("test_app", "Test Application", test_data_path)
    return app


@pytest.fixture
def test_config_file(temp_dir):
    config_content = """
    [test]
    value = "test_value"
    nested.value = "nested_test_value"
    """
    config_file = os.path.join(temp_dir, "test_config.toml")
    with open(config_file, "w") as f:
        f.write(config_content)
    return config_file
