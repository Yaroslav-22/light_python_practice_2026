import sys
import os
from scanner import scan_folder
from dublicat import poisk_dublicat

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

    print("Найдены файлы:")
    for f in files:
        print(f"Путь: {f['path']}, Размер: {f['size']} байт, Дата: {f['mtime']}")

    dublicat = poisk_dublicat([f['path'] for f in files])
    if not dublicat:
        print("Дубликатов нет")
    else:
        print(f"\nНайдено групп дубликатов: {len(dublicat)}")
        for h, paths in dublicat.items():
            print(f"\nХеш: {h}")
            for p in paths:
                print(f"  {p}")
if __name__ == "__main__":
    main()