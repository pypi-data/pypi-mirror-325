# packager/commands/addtobundle.py

import os
from pathlib import Path
from typing import Tuple, Optional
import stat
import click
class BundlePackageAdder:
    """Handles adding packages to existing bundles."""
    
    def __init__(self, config, verbose: bool = False):
        """
        Initialize BundlePackageAdder.
        
        Args:
            config: PackagerConfig instance
            verbose: Whether to enable verbose output
        """
        self.config = config
        self.verbose = verbose
        self.paths = config.get_paths()
    
    def _log(self, message: str) -> None:
        """Log message if verbose mode is enabled."""
        if self.verbose:
            print(message)

    def _check_bundle_exists(self, bundle_name: str) -> Tuple[bool, Optional[str]]:
        """
        Check if bundle exists.
        
        Args:
            bundle_name: Name of the bundle
            
        Returns:
            Tuple of (exists, error_message)
        """
        bundle_path = Path(self.paths['packages_path']) / bundle_name / 'bin'
        if not bundle_path.exists():
            return False, f"Bundle {bundle_name} not found at {bundle_path}"
        return True, None

    def _check_image_exists(self, package: str, version: str) -> Tuple[bool, str, Optional[str]]:
        """
        Check if image exists in configuration.
        
        Args:
            package: Package name
            version: Package version
            
        Returns:
            Tuple of (exists, image_path, error_message)
        """
        key = f"{package}__{version}"
        if "images" not in self.config.config or key not in self.config.config["images"]:
            return False, "", f"Package {package} version {version} not found in configuration"
        
        image_path = self.config.config["images"][key]
        if not Path(image_path).exists():
            return False, "", f"Image file not found at {image_path}"
            
        return True, image_path, None

    def _create_executable(self, bundle_name: str, package: str, image_path: str, aliases: list) -> Tuple[bool, Optional[str]]:
        """
        Create executable file for the package.
        
        Args:
            bundle_name: Name of the bundle
            package: Package name
            image_path: Path to the Singularity image
            
        Returns:
            Tuple of (success, error_message)
        """
        try:
            bundle_bin = Path(self.paths['packages_path']) / bundle_name / 'bin'
            exec_path = bundle_bin / f"{package}.exec"
            package_path = bundle_bin / package

            script_content = f"""#!/bin/bash
singularity exec "{image_path}" $(basename "$0") "$@"
"""
            # Create executable file
            with open(exec_path, 'w') as f:
                f.write(script_content)
            
            # Make executable
            exec_path.chmod(exec_path.stat().st_mode | stat.S_IRWXU | stat.S_IRGRP | stat.S_IXGRP)
            
            # Make symlink to exec_path called package_path
            for alias in aliases:
                if os.path.exists(bundle_bin / alias):
                    click.echo(f"INFO: Alias {alias} already exists, skipping", err=True)
                    continue
                try:
                    os.symlink(exec_path, bundle_bin / alias)
                    self._log(f"Created alias: {alias}")
                except Exception as e:
                    click.echo(f"ERROR: Failed to create alias {alias}: {str(e)}", err=True)


            
            try:
                if os.path.exists(package_path):
                    click.echo(f"INFO: Executable {package} already exists, skipping", err=True)
                else:
                    os.symlink(exec_path, package_path)
                    self._log(f"Created executable: {exec_path}")
            except Exception as e:
                click.echo(f"ERROR: Failed to create executable: {str(e)}", err=True) 
            return True, None
            
        except Exception as e:
            return False, f"Failed to create executable: {str(e)}"

    def add_package_to_bundle(self, bundle_name: str, package: str, version: str, force = False,aliases = []) -> Tuple[str, str]:
        """
        Add a package to a bundle.
        
        Args:
            bundle_name: Name of the bundle
            package: Package name
            version: Package version
            
        Returns:
            Tuple of (status, message)
            Status can be: "success", "error"
        """
        # Check if bundle exists
        exists, error = self._check_bundle_exists(bundle_name)
        if not exists:
            return "error", error
            
        # Check if image exists
        exists, image_path, error = self._check_image_exists(package, version)
        if not exists:
            return "error", error
            
        # Create executable
        success, error = self._create_executable(bundle_name, package, image_path, aliases)
        if not success:
            return "error", error
            
        return "success", f"Added {package} version {version} to bundle {bundle_name}"

def add_to_bundle_command(config, bundle_name: str, package: str, version: str, 
                            force: bool,
                         verbose: bool,
                         aliases: list) -> Tuple[str, str]:
    """
    Main entry point for the addtobundle command.
    
    Args:
        config: PackagerConfig instance
        bundle_name: Name of the bundle
        package: Package name
        version: Package version
        verbose: Whether to enable verbose output
        
    Returns:
        Tuple of (status, message)
        Status can be: "success", "error"
    """
    adder = BundlePackageAdder(config, verbose)
    return adder.add_package_to_bundle(bundle_name, package, version, force, aliases)