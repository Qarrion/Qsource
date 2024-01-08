

import asyncio
import time
import logging
class data:

    def __init__(self, logger:logging.Logger):
        self.x = 0
        self.logger = logger

    async def instance_x(self, x):
        self.x=x
        await asyncio.sleep(3)
        self.logger.info(self.x)

    async def local_x(self, x):
        x=x
        await asyncio.sleep(3)
        self.logger.info(x)

        

if __name__ == "__main__":
    from Qlogger import Logger
    logger = Logger('test', 'blue')
    d=data(logger)

    async def main():
        # task1 = asyncio.create_task(d.instance_x(3))
        # task2 = asyncio.create_task(d.instance_x(2))
        task1 = asyncio.create_task(d.local_x(3))
        task2 = asyncio.create_task(d.local_x(2))
    
        await task1
        await task2
    

    asyncio.run(main())