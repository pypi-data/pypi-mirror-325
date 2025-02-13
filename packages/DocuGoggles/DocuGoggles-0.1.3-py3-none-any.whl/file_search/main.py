from file_search.file_scanner.scanner import FileScanner
import os

def main():
    default_dir = "/home"  
    print(f"\nCurrent directory: {default_dir}")
    custom_dir = input("Press Enter to use current directory or enter a new path: ").strip()
    directory_to_scan = custom_dir if custom_dir else default_dir
    
    # Create instance for the scanner class (scanner.py)
    scanner = FileScanner(directory_to_scan)
    
    print(f"\nScanning directory for all files: {directory_to_scan}")
    print("=" * 50)
    
    # Scan for all files ( for specific file types, pass a list of extensions instead of None)
    files = scanner.scan_directory(None)
    
    if not files:
        print("No files found in the directory.")
        return
        
    total_files = 0
    for extension, file_list in files.items():
        if file_list:
            file_count = len(file_list)
            total_files += file_count
            print(f"\nFile type: {extension if extension else 'No extension'}")
            print(f"Count: {file_count}")
    
    print(f"\nSummary:")
    print(f"Total files found: {total_files}")
    print(f"Unique file types: {len(files)}")

if __name__ == "__main__":
    main()