# packager/commands/scanpackages.py
import os
import re
from pathlib import Path
from typing import List, Dict, Tuple, Optional
import click
class PackagePatterns:
    """Defines patterns for package name and version extraction."""
    
    VALID_PATTERNS = [
        r'singularity-(.+?)__(.+?)--',  # Main pattern for package detection
        r'depot\.galaxyproject\.org-singularity-(.+?)-(.+?)--', # Galaxy pattern
        r'(.+?)__(.+?)\d?'  # Generic pattern
    ]
    
    VALID_EXTENSIONS = [
        '.simg',
        '.img',
        '.sif'
    ]
    
    @classmethod
    def is_valid_extension(cls, filename: str) -> bool:
        """Check if file has a valid Singularity image extension."""
        return any(filename.endswith(ext) for ext in cls.VALID_EXTENSIONS)
    
    @classmethod
    def extract_package_info(cls, filename: str) -> Optional[Tuple[str, str]]:
        """
        Extract package name and version from filename.
        
        Args:
            filename: Name of the file to parse
            
        Returns:
            Tuple of (package_name, version) or None if no match
        """
        for pattern in cls.VALID_PATTERNS:
            match = re.search(pattern, filename)
            if match and len(match.groups()) >= 2:
                return match.group(1), match.group(2)
        return None

class PackageScanner:
    """Handles scanning directories for Singularity packages."""
    
    def __init__(self, config, force: bool = False):
        """
        Initialize PackageScanner.
        
        Args:
            config: PackagerConfig instance
            force: Whether to overwrite existing entries
        """
        self.config = config
        self.force = force
        self.found_packages: Dict[str, str] = {}
        self.skipped_packages: Dict[str, str] = {}
    
    def scan_directory(self, directory: str, verbose = False) -> Tuple[int, int]:
        """
        Scan directory for Singularity packages.
        
        Args:
            directory: Directory path to scan
            
        Returns:
            Tuple of (packages_added, packages_skipped)
        """
        directory_path = Path(directory).resolve()
        if not directory_path.exists():
            raise FileNotFoundError(f"Directory not found: {directory}")
        
        if not directory_path.is_dir():
            raise NotADirectoryError(f"Not a directory: {directory}")
        
        # Scan all files in directory
        for filepath in directory_path.glob('*'):
            if filepath.is_file() and PackagePatterns.is_valid_extension(filepath.name):
                if not filepath.stat().st_size:
                    continue
                if verbose:
                    click.echo(f"Processing {filepath}")
                self._process_file(filepath)
        
        # Update configuration
        self._update_config()
        
        return len(self.found_packages), len(self.skipped_packages)
    
    def _process_file(self, filepath: Path) -> None:
        """Process a single file and extract package information."""
        package_info = PackagePatterns.extract_package_info(filepath.name)
        if package_info:
            name, version = package_info
            key = f"{name}__{version}"
            
            # Check if package already exists in config
            if not self.force and key in self.config.config["images"]:
                self.skipped_packages[key] = str(filepath)
            else:
                self.found_packages[key] = str(filepath)
    
    def _update_config(self) -> None:
        """Update configuration with found packages."""
        for key, path in self.found_packages.items():
            name, version = key.split("__")
            self.config.add_image(name, version, path)

def scan_packages_command(config, directory: Optional[str] = None, force: bool = False, verbose: bool = False) -> Tuple[int, int, Dict[str, str]]:
    """
    Main entry point for the scanpackages command.
    
    Args:
        config: PackagerConfig instance
        directory: Optional directory to scan (uses config default if not provided)
        force: Whether to overwrite existing entries
        
    Returns:
        Tuple of (packages_added, packages_skipped, skipped_packages_dict)
    """
    scanner = PackageScanner(config, force)
    scan_dir = directory or config.config["packager"]["singularity_path"]
    
    try:
        added, skipped = scanner.scan_directory(scan_dir, verbose)
        return added, skipped, scanner.skipped_packages
    except (FileNotFoundError, NotADirectoryError) as e:
        raise click.ClickException(str(e))