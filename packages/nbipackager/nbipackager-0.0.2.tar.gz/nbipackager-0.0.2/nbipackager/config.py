import os
import configparser
from pathlib import Path

class PackagerConfig:
    def __init__(self):
        self.config_file = os.path.expanduser("~/.config/packager.ini")
        # Disable interpolation to handle special characters in paths
        self.config = configparser.ConfigParser(interpolation=None)
        self.load_config()

    def load_config(self):
        """Load configuration from file."""
        if os.path.exists(self.config_file):
            self.config.read(self.config_file)
        else:
            self._create_default_config()

    def _create_default_config(self):
        """Create default configuration file."""
        self.config["packager"] = {
            "singularity_path": "/qib/platforms/Informatics/transfer/outgoing/singularity/nxf/",
            "bin_path": "/nbi/software/testing/bin/",
            "packages_path": "/nbi/software/testing/"
        }
        self.config["images"] = {}
        self.save_config()

    def save_config(self):
        """Save configuration to file."""
        os.makedirs(os.path.dirname(self.config_file), exist_ok=True)
        with open(self.config_file, 'w') as configfile:
            self.config.write(configfile)

    def add_image(self, name: str, version: str, path: str):
        """Add an image to the configuration."""
        if "images" not in self.config:
            self.config["images"] = {}
        self.config["images"][f"{name}__{version}"] = path
        self.save_config()

    def get_image_path(self, name: str, version: str) -> str:
        """Get image path from configuration."""
        key = f"{name}__{version}"
        return self.config["images"].get(key)

    def get_paths(self) -> dict:
        """Get paths from configuration."""
        return {
            "singularity_path": self.config["packager"]["singularity_path"],
            "bin_path": self.config["packager"]["bin_path"],
            "packages_path": self.config["packager"]["packages_path"]
        }