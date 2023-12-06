import asyncio
import time

async def say_after(delay, what):
    print("in")
    await asyncio.sleep(delay)
    print("again")
    print(what)

async def main():

    tasks = list()
    task1 = asyncio.create_task(
        say_after(5, 'hello'))

    task2 = asyncio.create_task(
        say_after(6, 'world'))

    print(f"started at {time.strftime('%X')}")

    await task1
    await task2

    print(f"finished at {time.strftime('%X')}")

#? task : asyncio.create_task
