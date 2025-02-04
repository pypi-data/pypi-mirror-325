import os
import shutil

def organize_files(directory):
    """Organizes files into subfolders based on their extensions."""
    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)
        if os.path.isfile(file_path):
            ext = file.split(".")[-1]
            folder_path = os.path.join(directory, ext)
            os.makedirs(folder_path, exist_ok=True)
            shutil.move(file_path, os.path.join(folder_path, file))
            print(f"Moved {file} -> {folder_path}/")

if __name__ == "__main__":
    organize_files("downloads")  # Change "downloads" to your directory

