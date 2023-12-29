import asyncio
import datetime
import random
import websockets

CONNECTIONS = set()

async def register(websocket):
    CONNECTIONS.add(websocket)
    try:
        await websocket.wait_closed()
    finally:
        CONNECTIONS.remove(websocket)

async def show_time():
    while True:
        message = datetime.datetime.utcnow().isoformat() + "Z"
        print(message)
        websockets.broadcast(CONNECTIONS, message)
        await asyncio.sleep(3)

async def main():
    async with websockets.serve(register, "localhost", 5678):
        await show_time()

if __name__ == "__main__":
    asyncio.run(main())