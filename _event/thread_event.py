import threading

stop_event = threading.Event()

print(f"stop_event: {stop_event.is_set()}")
print(f"stop_event.wait: {stop_event.wait(2)}")
cnt = 0
while not stop_event.is_set():
    cnt += 1
    print(f"hi - {cnt}")
    if cnt == 5:
        stop_event.set()
        print("stop_event set!")
        print(f"stop_event: {stop_event.is_set()}")