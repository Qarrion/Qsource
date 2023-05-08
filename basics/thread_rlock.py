# from q_logging import e01_logging_color as log

# ---------------------------------------------------------------------------- #
import logging

# 로그 레벨을 설정합니다.
base_format = '%(asctime)s - %(threadName)s(%(thread)d) - %(levelname)s - %(message)s'

# logging.getLogger().setLevel(logging.DEBUG)
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

def worker(lock,logger:logging.Logger):
    logger.info("Trying to acquire lock...")
    lock.acquire()
    logger.info("Lock acquired!")
    logger.info("Trying to acquire again...")
    lock.acquire()
    logger.info("Lock re-acquired!")
    lock.release()
    logger.info("Lock released!")
    lock.release()
    logger.info("Lock released again!")

lock = threading.RLock()

thread1 = threading.Thread(target=worker, args=(lock,blue))
thread2 = threading.Thread(target=worker, args=(lock,green))

thread1.start()
thread2.start()

thread1.join()
thread2.join()