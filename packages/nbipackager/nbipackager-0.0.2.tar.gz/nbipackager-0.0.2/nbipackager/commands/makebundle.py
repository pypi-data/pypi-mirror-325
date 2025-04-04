# packager/commands/makebundle.py
import os
from pathlib import Path
from typing import Tuple, Optional
import stat

class BundleCreator:
    """Handles the creation of bundle directories and files."""
    
    def __init__(self, config, verbose: bool = False):
        """
        Initialize BundleCreator.
        
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

    def _check_existing(self, name: str) -> Tuple[bool, Optional[str]]:
        """
        Check if bundle already exists.
        
        Args:
            name: Bundle name
            
        Returns:
            Tuple of (exists, path_that_exists)
        """
        nbi_path = Path(self.paths['packages_path']) / name / 'bin'
        bin_path = Path(self.paths['bin_path']) / name
        
        if nbi_path.exists():
            return True, str(nbi_path)
        if bin_path.exists():
            return True, str(bin_path)
            
        return False, None

    def _create_bundle_directory(self, name: str) -> Tuple[bool, Optional[str]]:
        """
        Create bundle directory structure.
        
        Args:
            name: Bundle name
            
        Returns:
            Tuple of (success, error_message)
        """
        try:
            nbi_path = Path(self.paths['packages_path']) / name / 'bin'
            nbi_path.mkdir(parents=True, exist_ok=True)
            self._log(f"Created directory: {nbi_path}")
            return True, None
        except Exception as e:
            return False, f"Failed to create bundle directory: {str(e)}"

    def _create_bundle_script(self, name: str) -> Tuple[bool, Optional[str]]:
        """
        Create bundle script file.
        
        Args:
            name: Bundle name. Will be used as the script filename in bin_path
            
        Returns:
            Tuple of (success, error_message)
        """
        try:
            # Path to the bundle's bin directory that will be added to PATH
            bundle_bin_path = Path(self.paths['packages_path']) / name / 'bin'
            
            # Path to the script file we're creating
            script_file_path = Path(self.paths['bin_path']) / name
            
            script_content = f"""#!/bin/bash
# Made by NBIPACKAGER
export PATH={bundle_bin_path}:"$PATH"
"""
            # Create and write to the script file using 'with open'
            with open(script_file_path, 'w') as f:
                f.write(script_content)
            
            # Make the script file executable
            script_file_path.chmod(script_file_path.stat().st_mode | stat.S_IRWXU | stat.S_IRGRP | stat.S_IXGRP)
            
            self._log(f"Created script file: {script_file_path}")
            return True, None
        except Exception as e:
            return False, f"Failed to create bundle script: {str(e)}"

    def create_bundle(self, name: str, force: bool = False) -> Tuple[str, str]:
        """
        Create a new bundle.
        
        Args:
            name: Bundle name
            force: Whether to overwrite existing entries
            
        Returns:
            Tuple of (status, message)
            Status can be: "success", "exists", "error"
        """
        # Validate bundle name
        if not name or not name.replace("_", "").isalnum():
            return "error", "Invalid bundle name. Use only alphanumeric characters and underscores."

        # Check if bundle exists
        exists, existing_path = self._check_existing(name)
        if exists and not force:
            return "exists", f"Bundle already exists at: {existing_path}"
        
        # Create bundle directory
        success, error = self._create_bundle_directory(name)
        if not success:
            return "error", error
            
        # Create bundle script
        success, error = self._create_bundle_script(name)
        if not success:
            return "error", error
            
        return "success", f"Bundle '{name}' created successfully"

def make_nbi_bundle_command(config, name: str, force: bool = False, verbose: bool = False, 
                         package_versions: dict = None) -> Tuple[str, str]:
    """
    Main entry point for the makebundle command.
    
    Args:
        config: PackagerConfig instance
        name: Bundle name
        force: Whether to overwrite existing entries
        verbose: Whether to enable verbose output
        package_versions: Dictionary of package names and their versions to add
        
    Returns:
        Tuple of (status, message)
        Status can be: "success", "exists", "error"
    """
    creator = BundleCreator(config, verbose)
    status, message = creator.create_bundle(name, force)
    
    if status == "success" and package_versions:
        # If bundle was created successfully and we have packages to add,
        # add them using addtobundle command
        from .addtobundle import add_to_bundle_command
        for package, version in package_versions.items():
            pkg_status, pkg_message = add_to_bundle_command(config, name, package, version)
            if pkg_status != "success":
                return "error", f"Failed to add package {package}: {pkg_message}"
        
        message = f"{message}\nAdded {len(package_versions)} package(s) to bundle"
    
    return status, message