import pandas as pd

def process_uploaded_files(file_paths):
    data_frames = {}
    for file_path in file_paths:
        if file_path.endswith(('.xlsx', '.xlsm')):
            df = pd.read_excel(file_path)
        elif file_path.endswith('.csv'):
            encoding = detect_encoding(file_path)
            with open(file_path, 'r', encoding=encoding, errors='ignore') as f:
                df = pd.read_csv(f, on_bad_lines='skip')
        else:
            raise ValueError(f"Unsupported file format: {file_path}")

        data_frames[file_path] = df

    return data_frames

def detect_encoding(file_path):
    import chardet
    with open(file_path, 'rb') as f:
        result = chardet.detect(f.read())
        return result['encoding']