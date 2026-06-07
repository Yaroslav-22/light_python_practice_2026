import sys
import os

def main():
    if len(sys.argv) < 2:
        print("Использование: python main.py <путь_к_папке>")
        sys.exit(1)

    target_folder = sys.argv[1]

    if not os.path.isdir(target_folder):
        print(f"Ошибка: папка '{target_folder}' не существует или недоступна.")
        sys.exit(1)

    print(f"Принят путь: {target_folder}")
    print("Этап 1 готов")

if __name__ == "__main__":
    main()