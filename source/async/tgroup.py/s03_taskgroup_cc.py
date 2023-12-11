import asyncio
import logging

import signal

class Limiter:
    def __init__(self, logger:logging.Logger):
        self.logger = logger
        self.stop_event = asyncio.Event()
        self.queue  = asyncio.Queue()

    async def worker(self, ith):

        while not self.stop_event.is_set():
            try:
                item = await asyncio.wait_for(self.queue.get(), timeout=1)
                self.logger.info(f"worker-{ith}, start work")
                await asyncio.sleep(5)
                self.logger.info(f"worker-{ith}, finish work")
            except asyncio.TimeoutError:
                continue
            except asyncio.CancelledError:
                raise KeyboardInterrupt
                # self.stop_event.set()
                # self.logger.info(f"worker-{ith}, set event")


    async def enqueue(self):
        for i in range(10):
            await self.queue.put(i)
        
if __name__=="__main__":
    logger = logging.getLogger('mylogger')
    logger.setLevel(logging.DEBUG) 
    handler = logging.StreamHandler() 
    handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    def signal_handler(sig, frame):
        print('Ctrl+C Interrupt!')
        limiter.stop_event.set()

    limiter = Limiter(logger)

    async def main():


        async with asyncio.TaskGroup() as tg:
            tasks = [tg.create_task(limiter.worker(i)) for i in range(5)]
            put = tg.create_task(limiter.enqueue())

        signal.signal(signal.SIGINT, signal_handler)
        
    asyncio.run(main())

