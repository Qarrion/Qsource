

import threading
import time
import logging
class data:

    def __init__(self, logger:logging.Logger):
        self.x = 0
        self.logger = logger

    def instance_x(self, x):
        self.x=x
        time.sleep(3)
        self.logger.info(self.x)

    def local_x(self, x):
        x=x
        time.sleep(3)
        self.logger.info(x)

        

if __name__ == "__main__":
    from Qlogger import Logger
    
    logger = Logger('test', 'blue')

    d=data(logger)
    # threading.Thread(target=d.instance_x, args=(3,)).start()
    # threading.Thread(target=d.instance_x, args=(2,)).start()
    threading.Thread(target=d.local_x, args=(3,)).start()
    threading.Thread(target=d.local_x, args=(2,)).start()
