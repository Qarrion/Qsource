

# ---------------------------------------------------------------------------- #
import logging

base_format = '%(asctime)s - %(threadName)s - %(levelname)s - %(message)s'

logging.basicConfig(format=base_format, level=logging.INFO)

logger = logging.getLogger()
logger.setLevel(logging.INFO)

import threading
import time


def myfunc(event:threading.Event):
    c = 0
    while not event.is_set():
        c += 1
        time.sleep(1)
        logger.info(f"hi - {c}")


if __name__ == "__main__":
    stop = threading.Event()    
    th1 = threading.Thread(target=myfunc, args=(stop,))
    th2 = threading.Thread(target=myfunc, args=(stop,))
    
    th1.start()
    th2.start()
    # th.join()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        stop.set()
        th1.join()
        th2.join()