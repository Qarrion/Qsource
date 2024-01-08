import asyncio
import websockets


import sys
args = sys.argv[1:]

# ---------------------------------------------------------------------------- #
#                                    1.Base                                    #
# ---------------------------------------------------------------------------- #
# 연결과 send를 구분하는 슬립
# ---------------------------------------------------------------------------- #
# async def connect():
#     uri = "ws://localhost:6789"

#     async with websockets.connect(uri) as websocket:
#         if len(args)>0:
#             msg = args[0]
#         else:
#             msg = 'hello'
#         if len(args)>1:
#             await asyncio.sleep(int(args[1]))
#         # if 
#         print(f">>> client msg send '{msg}'")
#         await websocket.send(msg)

#         async for msg in websocket:
#             print(f"<<< client msg recv '{msg}'")

# asyncio.run(connect())

# ---------------------------------------------------------------------------- #
#                                    2.loop                                    #
# ---------------------------------------------------------------------------- #
# Loop를 통해 낮은 수준 구현
# ---------------------------------------------------------------------------- #
async def connect():
    uri = "ws://localhost:6789"

    async with websockets.connect(uri) as websocket:
        # cumstom ---------------------------
        if len(args)>0:
            msg = args[0]
        else:
            msg = 'hello'
        if len(args)>1:
            await asyncio.sleep(int(args[1]))
        #------------------------------------
        print(f">>> client msg send '{msg}'")
        await websocket.send(msg)

        # async for msg in websocket:
        while True:
            msg = await websocket.recv()
            print(f"<<< client msg recv '{msg}'")

asyncio.run(connect())