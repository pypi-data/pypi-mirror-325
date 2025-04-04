# packager/commands/addpackage.py
import os
from pathlib import Path
from typing import Optional, Tuple

class PackageValidator:
    """Validates package information before adding to configuration."""
    
    @staticmethod
    def validate_image_path(image_path: str) -> Tuple[bool, Optional[str]]:
        """
        Validate that the image path exists and is a file.
        
        Args:
            image_path: Path to the Singularity image
            
        Returns:
            Tuple of (is_valid, error_message)
        """
        if not os.path.exists(image_path):
            return False, f"Image path does not exist: {image_path}"
        
        if not os.path.isfile(image_path):
            return False, f"Image path is not a file: {image_path}"
            
        return True, None

    @staticmethod
    def validate_name(name: str) -> Tuple[bool, Optional[str]]:
        """
        Validate package name format.
        
        Args:
            name: Package name to validate
            
        Returns:
            Tuple of (is_valid, error_message)
        """
        if not name:
            return False, "Package name cannot be empty"
            
        if not name.replace("_", "").isalnum():
            return False, "Package name can only contain alphanumeric characters and underscores"
            
        return True, None

    @staticmethod
    def validate_version(version: str) -> Tuple[bool, Optional[str]]:
        """
        Validate version format.
        
        Args:
            version: Version string to validate
            
        Returns:
            Tuple of (is_valid, error_message)
        """
        if not version:
            return False, "Version cannot be empty"
            
        if not all(part.replace(".", "").isalnum() for part in version.split(".")):
            return False, "Version can only contain alphanumeric characters and dots"
            
        return True, None

class PackageAdder:
    """Handles the addition of packages to the configuration."""
    
    def __init__(self, config):
        """
        Initialize PackageAdder.
        
        Args:
            config: PackagerConfig instance
        """
        self.config = config
        self.validator = PackageValidator()

    def add_package(self, image: str, name: str, version: str) -> Tuple[bool, Optional[str]]:
        """
        Add a package to the configuration.
        
        Args:
            image: Path to the Singularity image
            name: Package name
            version: Package version
            
        Returns:
            Tuple of (success, error_message)
        """
        # Validate inputs
        for validator, value in [
            (self.validator.validate_image_path, image),
            (self.validator.validate_name, name),
            (self.validator.validate_version, version)
        ]:
            is_valid, error = validator(value)
            if not is_valid:
                return False, error

        # Check if package already exists
        package_key = f"{name}__{version}"
        if package_key in self.config.config["images"]:
            return False, f"Package {name} version {version} already exists in configuration"

        try:
            # Add package to configuration
            self.config.add_image(name, version, image)
            return True, None
        except Exception as e:
            return False, f"Failed to add package: {str(e)}"

def add_package_command(config, image: str, name: str, version: str) -> Tuple[bool, Optional[str]]:
    """
    Main entry point for the addpackage command.
    
    Args:
        config: PackagerConfig instance
        image: Path to the Singularity image
        name: Package name
        version: Package version
        
    Returns:
        Tuple of (success, error_message)
    """
    adder = PackageAdder(config)
    return adder.add_package(image, name, version)