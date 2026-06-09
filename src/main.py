import sys
import os
from scanner import scan_folder

def main():
    if len(sys.argv) < 2:
        print("Использование: python main.py <путь_к_папке>")
        sys.exit(1)

    target_folder = sys.argv[1]

    if not os.path.isdir(target_folder):
        print(f"Ошибка: папка '{target_folder}' не существует или недоступна.")
        sys.exit(1)

    print(f"Принят путь: {target_folder}")
    print(f"Сканирование папки: {target_folder}\n")

    files = scan_folder(target_folder)

    print(f"Найдено файлов: {len(files)}\n")
    print("Список файлов (путь | размер (байт) | дата изменения):")
    print("-" * 80)

    for f in files:
        path_short = f['path'] if len(f['path']) < 60 else '...' + f['path'][-57:]
        print(f"{path_short:<60} | {f['size']:>10} | {f['mtime']}")

if __name__ == "__main__":
    main()