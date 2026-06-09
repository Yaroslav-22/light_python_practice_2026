import datetime
import os

def scan_folder(folder_path):
    files_data = []

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            full_path = os.path.join(root, file)
            try:
                size = os.path.getsize(full_path)
                mtime_timestamp = os.path.getmtime(full_path)
                mtime_str = datetime.datetime.fromtimestamp(mtime_timestamp).strftime('%Y-%m-%d %H:%M:%S')

                files_data.append({
                    'path': full_path,
                    'size': size,
                    'mtime': mtime_str
                })
            except (OSError, PermissionError) as e:
                print(f"Предупреждение: не удалось прочитать {full_path} - {e}")
                continue
    return files_data