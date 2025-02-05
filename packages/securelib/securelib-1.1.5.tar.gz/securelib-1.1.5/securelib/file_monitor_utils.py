import os
import hashlib

def detect_file_modifications(directory: str) -> dict:
    file_hashes = {}
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            with open(file_path, 'rb') as f:
                file_hash = hashlib.md5(f.read()).hexdigest()
            file_hashes[file_path] = file_hash
    return file_hashes
