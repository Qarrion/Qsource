import asyncio
import time

async def say_after(delay, what):
    print("in")
    await asyncio.sleep(delay)
    print("again")
    print(what)

async def main():

    task1 = asyncio.create_task(
        say_after(5, 'task1'))

    task2 = asyncio.create_task(
        say_after(6, 'task2'))

    print(f"started at {time.strftime('%X')}")

    await task1                 # task
    await task2                 # task  
    await say_after(5, 'corou') # coroutine


    print(f"finished at {time.strftime('%X')}")
asyncio.run(main())