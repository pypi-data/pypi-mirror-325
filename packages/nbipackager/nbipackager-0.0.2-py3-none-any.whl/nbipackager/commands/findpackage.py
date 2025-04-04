# packager/commands/findpackage.py

from typing import List, Tuple
import re

class PackageFinder:
    """Handles searching for packages in configuration."""
    
    def __init__(self, config):
        """
        Initialize PackageFinder.
        
        Args:
            config: PackagerConfig instance
        """
        self.config = config

    def find_packages(self, search_term: str, verbose: bool) -> List[Tuple[str, str]]:
        """
        Search for packages matching the search term.
        
        Args:
            search_term: String to search for in package names
            
        Returns:
            List of tuples (package_name, version)
        """
        if "images" not in self.config.config:
            return []

        matches = []
        pattern = re.compile(search_term, re.IGNORECASE)
        
        for key in self.config.config["images"]:
            try:
                package, version = key.split("__")
                if pattern.search(package):
                    matches.append((package, version))
            except ValueError:
                continue  # Skip malformed keys
                
        # Sort by package name and version
        return sorted(matches, key=lambda x: (x[0], x[1]))

def find_package_command(config, search_term: str, verbose: bool) -> List[Tuple[str, str]]:
    """
    Main entry point for the findpackage command.
    
    Args:
        config: PackagerConfig instance
        search_term: String to search for
        
    Returns:
        List of matching (package_name, version) tuples
    """
    finder = PackageFinder(config)
    return finder.find_packages(search_term, verbose)