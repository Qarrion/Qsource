import asyncio
import time

async def say_after(delay, what):
    print("in")
    await asyncio.sleep(delay)
    print("again")
    print(what)

async def main():

    # func = list()
    # task1 = asyncio.create_task(
    #     say_after(5, 'hello'))

    # task2 = asyncio.create_task(
    #     say_after(6, 'world'))

    # print(f"started at {time.strftime('%X')}")
    # tasks.append(task1)
    # tasks.append(task2)

    async with asyncio.TaskGroup() as tg: # exit await, + block 
        tasks = [tg.create_task(say_after(5,'hello')) for i in [5,6]]


    print(f"finished at {time.strftime('%X')}")
asyncio.run(main())
