import time

def tail_log(file_path):
    """Monitor a log file and print new lines as they are added."""
    with open(file_path, "r") as file:
        file.seek(0, 2)  # Move to the end of the file
        while True:
            line = file.readline()
            if line:
                print(line.strip())
            else:
                time.sleep(1)

if __name__ == "__main__":
    log_file = "app.log"  # Change this to your log file path
    tail_log(log_file)

