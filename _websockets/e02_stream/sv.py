import asyncio
import websockets
import traceback

# ---------------------------------------------------------------------------- #
#                                   1.Stream                                   #
# ---------------------------------------------------------------------------- #
import datetime
def now_str():
    now = datetime.datetime.now()
    now_str = now.strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
    return f"[{now_str}] "

async def conn_handler(websocket,path):
    # async for msg in websocket:
    client = websocket.remote_address
    print(f"client '{client}' connected")
    try:
        while True:
            msg = await websocket.recv()
            print(f"<<< server msg recv '{msg}'")
            await asyncio.sleep(30)
            while True:
                print(f"{now_str()} >>> server msg send '{msg}'")
                await websocket.send(msg+' sv')
                await asyncio.sleep(5)

    except websockets.exceptions.ConnectionClosed as e:
        print(f"client '{client}' disconnected. with exceptions: {e}")

    except Exception as e:
        traceback.format_exc()
        print(f"error : {e} '{type(e).__name__}' ")
async def main():
    async with websockets.serve(conn_handler, "localhost", 6789):
        await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())