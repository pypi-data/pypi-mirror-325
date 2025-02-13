import configparser
import json
import os
from pathlib import Path


DEFAULTS = {
    "logging": {
        "level": "INFO",
        "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    },
    "plugin_manager": {
        "plugin_dirs": []
    }
}


class Config:
    def __init__(self, app_root: Path, production: bool = False):
        self.app_root = Path(app_root)
        self.production = production

        # App directory config (defaults)
        self.app_config_dir = self.app_root / "config"
        self.app_config_file = self.app_config_dir / "settings.ini"
        self.app_plugin_dir = self.app_root / "plugins"

        # User directory config
        self.user_config_dir = self._get_user_config_dir(self.app_root.name)
        self.user_config_file = self.user_config_dir / "settings.ini"
        self.user_plugin_dir = self.user_config_dir / "plugins"

        self.config = self._load_config()
        self._apply_defaults()

    def _apply_defaults(self):
        # Dynamically set plugin_dirs default based on environment
        default_plugin_dirs = [str(self.app_plugin_dir.resolve())]
        if self.production:
            default_plugin_dirs.append(str(self.user_plugin_dir.resolve()))
        DEFAULTS["plugin_manager"]["plugin_dirs"] = default_plugin_dirs

        # Apply defaults only for missing keys
        for section, options in DEFAULTS.items():
            if not self.config.has_section(section):
                self.config.add_section(section)
            for key, value in options.items():
                if not self.config.has_option(section, key):
                    self.write_list(section, key, value)

    def _save_config(self):
        """Save the current configuration to the appropriate file"""
        config_file = self.user_config_file if self.production else self.app_config_file
        with open(config_file, 'w') as f:
            self.config.write(f)

    def _get_user_config_dir(self, app_name: str) -> Path:
        if os.name == 'nt':
            base = Path(os.environ['APPDATA'])
        else:
            base = Path.home() / ".config"
        return base / app_name

    def _load_config(self):
        # Create necessary directories
        self.app_config_dir.mkdir(exist_ok=True)
        if self.production:
            self.user_config_dir.mkdir(parents=True, exist_ok=True)

        # Choose which config file to use
        config_file = self.app_config_file if not self.production else self.user_config_file

        # If in production and user config doesn't exist, copy defaults
        if self.production and not self.user_config_file.exists():
            self._copy_default_to_user()

        config = configparser.ConfigParser()
        config.read(config_file)
        return config

    def _copy_default_to_user(self):
        import shutil
        shutil.copy2(self.app_config_file, self.user_config_file)

    def save(self):
        """Explicitly save configuration changes."""
        self._save_config()

    def write_list(self, section, option, data_list):
        """Write a list to the config as a JSON string."""
        if not self.config.has_section(section):
            self.config.add_section(section)
        self.config.set(section, option, json.dumps(data_list))

    def read_list(self, section, option):
        """Read a list from the config stored as a JSON string."""
        try:
            return json.loads(self.config.get(section, option))
        except (configparser.NoSectionError, configparser.NoOptionError, json.JSONDecodeError):
            return []  # Return an empty list if the key/section doesn't exist or is invalid

    def has_section(self, *args, **kwargs) -> bool:
        return self.config.has_section(*args, **kwargs)

    def add_section(self, *args, **kwargs):
        self.config.add_section(*args, **kwargs)

    def set(self, *args, **kwargs):
        self.config.set(*args, **kwargs)
