import os
from datetime import datetime
import chardet

def generate_unique_filename(directory, filename):
    base, extension = os.path.splitext(filename)
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    unique_filename = f"{base}_{timestamp}{extension}"
    return unique_filename

def detect_encoding(file_path):
    with open(file_path, 'rb') as f:
        result = chardet.detect(f.read(10000))
    return result['encoding']