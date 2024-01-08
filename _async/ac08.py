import asyncio

async def say_after(delay, what):
    print("in")
    await asyncio.sleep(delay)
    print("again")
    print(what)



async def main():
    # 이미 실행됨
    task1 = asyncio.create_task(
        say_after(1, 'task1'))

asyncio.run(main())
