from concurrent.futures import ThreadPoolExecutor
import threading
import time

def thread_task(stop_event):
    while not stop_event.is_set():
        try:
            print("Working...")
            time.sleep(1)
        except Exception as e:
            print(f"Error in thread: {e}")
    print("Thread stopping")

stop_event = threading.Event()

executor = ThreadPoolExecutor(max_workers=5)
for _ in range(5):
    executor.submit(thread_task, stop_event)

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("KeyboardInterrupt received. Signaling threads to stop...")
    stop_event.set()

executor.shutdown(wait=True)
print("ThreadPoolExecutor has been shut down.")