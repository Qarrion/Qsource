

# ---------------------------------------------------------------------------- #
import logging

# 로그 레벨을 설정합니다.
base_format = '%(asctime)s - %(threadName)s - %(levelname)s - %(message)s'

logging.getLogger().setLevel(logging.INFO)

# logger1을 생성하고 콘솔 핸들러를 추가합니다.
green = logging.getLogger('logger1')
console_handler1 = logging.StreamHandler()
console_handler1.setLevel(logging.DEBUG)
formatter1 = logging.Formatter(f'\033[32m{base_format}\033[0m')  # 녹색
console_handler1.setFormatter(formatter1)
green.addHandler(console_handler1)

# logger2를 생성하고 콘솔 핸들러를 추가합니다.
blue = logging.getLogger('logger2')
console_handler2 = logging.StreamHandler()
console_handler2.setLevel(logging.DEBUG)
formatter2 = logging.Formatter(f'\033[34m{base_format}\033[0m')  # 파란색
console_handler2.setFormatter(formatter2)
blue.addHandler(console_handler2)

# ---------------------------------------------------------------------------- #
import threading
import time


event=threading.Event()
print("----------------init")
print(event.is_set())

print("----------------set")
event.set()
print(event.is_set())

print("----------------clear")
event.clear()
print(event.is_set())

def producer(evt:threading.Event):
    time.sleep(3)
    green.info("set event")
    evt.set()

def consumer(evt:threading.Event):
    blue.info("start waiting")
    evt.wait()
    blue.info("finish waiting")


e_wait = threading.Event()
th1 = threading.Thread(target=consumer, args=(e_wait,), name='consumer')
th2 = threading.Thread(target=producer, args=(e_wait,), name='producer')

threads = []
threads.append(th1)
threads.append(th2)

for th in threads:
    th.start()

for th in threads:
    th.join()