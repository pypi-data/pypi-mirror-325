import shutil
import datetime

def backup_directory(source_dir, backup_dir="backup"):
    """Creates a timestamped backup of a directory."""
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    backup_path = f"{backup_dir}/backup_{timestamp}.zip"
    shutil.make_archive(backup_path, 'zip', source_dir)
    print(f"Backup created: {backup_path}")

if __name__ == "__main__":
    backup_directory("data")  # Change "data" to the folder you want to back up

