import asyncio
import logging

class limiter:

    def __init__(self, logger:logging.Logger):
        self.logger = logger
        self.queue = asyncio.Queue()
        self.stop_event = asyncio.Event()

    async def enqueue_coro(self, item):
        self.logger.info(f"put item-{item}")
        await self.queue.put(item)

    async def consume_coro(self, id):
        while not self.stop_event.is_set():
            try:
                item = await asyncio.wait_for(self.queue.get(), timeout=1)
                self.logger.info(f"coro-{id} processing item-{item} +")
                await asyncio.sleep(1)
                self.logger.info(f"coro-{id} processing item-{item} -")
                self.queue.task_done()
            except asyncio.TimeoutError:
                continue
            except asyncio.CancelledError:
                break # 
        self.logger.info(f"coro-{id} quit consume_coro")


    
if __name__ == "__main__":

    logger = logging.getLogger('mylogger')
    logger.setLevel(logging.DEBUG) 
    handler = logging.StreamHandler() 
    handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    lim = limiter(logger)
    async def main():

        for i in range(10):
            await lim.enqueue_coro(i)
    
    
        async with asyncio.TaskGroup() as tg:
            tasks = [tg.create_task(lim.consume_coro(i)) for i in range(5)]


    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("Received exit signal, shutting down...")
        # lim.stop_event.set()    

        # for task in asyncio.all_tasks():
        #     print(task)
        #     print(f"{task.get_name}  {task.done()}")
        #     if task is not asyncio.current_task():
        #         task.cancel()