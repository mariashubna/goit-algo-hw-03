from pathlib import Path
import shutil

def file_sort(path1: Path, path2: Path):
    for child in path1.iterdir():
        if child.is_dir():
            file_sort(child, path2)
        else:
            names = child.name
            for char in names:
                if char == '.':
                    file_extension = names.split('.')[-1]
                    file_dir = path2 / file_extension
            
            file_dir.mkdir(parents=True, exist_ok=True)
            shutil.move(str(child), str(f'{file_dir}/{child.name}'))

            

if __name__ == "__main__":
    path1 = input("Ім'я поточної папки ")
    path2 = input("Ім'я папки для переміщення ") or 'dict'
    root = Path(path1)
    destination = Path(path2)

    try:
        file_sort(root, destination)
        print("File sorting completed successfully.")
    except Exception as e:
        print(f"Error: {e}")
