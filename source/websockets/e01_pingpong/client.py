import asyncio
import websockets

async def send_ping():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as ws:
        # Send a ping

        await ws.send('hi')

        await ws.ping()
        await ws.pong()

        # await pong_waiter  # Wait for a pong response
        # await asyncio.wait_for(pong_waiter,timeout=10)

        print("Pong received!")

if __name__ == "__main__":
    asyncio.run(send_ping())