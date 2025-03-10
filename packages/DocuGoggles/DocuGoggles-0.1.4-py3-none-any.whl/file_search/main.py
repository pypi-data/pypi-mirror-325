from file_scanner.scanner import FileScanner
import os
from typing import Dict, List
from tabulate import tabulate

def format_file_count(count: int) -> str:
    """Format file count with thousands separator"""
    return f"{count:,}"

def categorize_extensions(files: Dict[str, List]) -> Dict[str, Dict[str, int]]:
    """Categorize file extensions into groups"""
    categories = {
        'Documents': ['.txt', '.pdf', '.doc', '.docx', '.xlsx', '.pptx', '.md', '.rst'],
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg', '.webp', '.ico', '.tiff'],
        'Code': ['.py', '.js', '.java', '.cpp', '.h', '.css', '.html', '.ts', '.jsx', '.php'],
        'Archives': ['.zip', '.rar', '.7z', '.tar', '.gz'],
        'Media': ['.mp3', '.mp4', '.wav', '.avi', '.mov', '.ogg'],
        'Data': ['.json', '.xml', '.csv', '.sql', '.db'],
        'Executables': ['.exe', '.dll', '.msi'],
        'Other': []
    }
    
    result = {category: {} for category in categories}
    
    for ext, files_list in files.items():
        categorized = False
        for category, extensions in categories.items():
            if ext.lower() in extensions:
                result[category][ext] = len(files_list)
                categorized = True
                break
        if not categorized:
            result['Other'][ext] = len(files_list)
    
    return result

def print_category_results(category_name: str, extensions: Dict[str, int]):
    """Print results for a specific category"""
    if not extensions:
        return
    
    # Prepare data for tabulate
    data = [[ext, format_file_count(count)] for ext, count in 
            sorted(extensions.items(), key=lambda x: x[1], reverse=True)]
    
    print(f"\n{category_name}")
    print("=" * len(category_name))
    print(tabulate(data, headers=['Extension', 'Count'], tablefmt='simple'))
    print(f"Total {category_name.lower()}: {format_file_count(sum(extensions.values()))}")

def main():
    default_dir = "/home"  
    print(f"\nCurrent directory: {default_dir}")
    custom_dir = input("Press Enter to use current directory or enter a new path: ").strip()
    directory_to_scan = custom_dir if custom_dir else default_dir
    
    # Create scanner instance
    scanner = FileScanner(directory_to_scan)
    
    print(f"\nScanning directory: {directory_to_scan}")
    print("=" * 50)
    
    try:
        # None for all files, or pass a list of extensions
        files = scanner.scan_directory([".txt"])
        
        if not files:
            print("\nNo files found in the directory.")
            return
        
        stats = scanner.get_directory_statistics()
        
        categorized_files = categorize_extensions(files)
        
        for category in categorized_files:
            print_category_results(category, categorized_files[category])
        
        # Print summary
        print("\nSummary")
        print("=======")
        print(f"Total files: {format_file_count(stats['total_files'])}")
        print(f"Total directories: {format_file_count(stats['total_directories'])}")
        print(f"Total size: {format_file_count(stats['total_size'])} bytes")
        print(f"Unique file types: {len(stats['extension_counts'])}")
        
    except FileNotFoundError:
        print(f"\nError: Directory '{directory_to_scan}' not found.")
    except Exception as e:
        print(f"\nError occurred: {str(e)}")

if __name__ == "__main__":
    main()