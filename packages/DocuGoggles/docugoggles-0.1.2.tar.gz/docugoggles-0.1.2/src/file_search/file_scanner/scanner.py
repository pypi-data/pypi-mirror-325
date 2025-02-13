import os
from pathlib import Path
from typing import List, Dict

class FileScanner:
    
    def __init__(self, base_directory: str):
        self.base_directory = Path(base_directory)
        
    def scan_directory(self, file_types: List[str] = None) -> Dict[str, List[str]]:
        """
        Scan the directory for files of specified types.
        Args:
            file_types: List of file extensions to scan for (e.g., ['.txt', '.pdf'])
                       If None, scans for all files.
        
        Returns:
            Dictionary with file types as keys and lists of file paths as values
        """
        if not self.base_directory.exists():
            raise FileNotFoundError(f"Directory not found: {self.base_directory}")
        
        found_files: Dict[str, List[str]] = {}
        
        for root, _, files in os.walk(self.base_directory):
            for file in files:
                file_path = Path(root) / file
                extension = file_path.suffix.lower() #

                
                if file_types is None or extension in file_types:
                    if extension not in found_files:
                        found_files[extension] = []
                    found_files[extension].append(str(file_path))
        
        return found_files

    def get_file_metadata(self, file_path: str) -> Dict[str, str]:

        path = Path(file_path)
        return {
            'name': path.name,
            'extension': path.suffix,
            'size': str(path.stat().st_size),
            'modified': str(path.stat().st_mtime),
            'path': str(path.absolute())
        }