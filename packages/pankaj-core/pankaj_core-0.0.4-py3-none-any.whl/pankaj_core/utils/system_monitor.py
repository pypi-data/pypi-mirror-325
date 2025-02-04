import psutil
import time

def system_monitor():
    """Monitor CPU and Memory usage every 2 seconds."""
    while True:
        cpu = psutil.cpu_percent(interval=1)
        memory = psutil.virtual_memory().percent
        print(f"CPU Usage: {cpu}% | Memory Usage: {memory}%")
        time.sleep(2)

if __name__ == "__main__":
    system_monitor()

