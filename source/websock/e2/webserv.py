# import asyncio
# import websockets
# import random
# import json

# async def handler(websocket, path):
#     while True:
#         # 100 ~ 2000 사이의 랜덤한 숫자를 연결된 유저에게 전송합니다.
#         number = random.randint(100, 2000)
#         print(number)
#         res = {
#             "number": number
#         }
#         await websocket.send(json.dumps(res))
#         await asyncio.sleep(1)

# async def main():
#     async with websockets.serve(handler, "localhost", 8080):
#         await asyncio.Future()

# asyncio.run(main())

import asyncio
import websockets
import random
import json

# 연결된 클라이언트의 수를 추적하는 전역 변수
connected_clients = 0

async def handler(websocket, path):
    global connected_clients
    connected_clients += 1  # 클라이언트 연결 시 카운트 증가

    try:
        while True:
            # 100 ~ 2000 사이의 랜덤한 숫자를 연결된 유저에게 전송합니다.
            number = random.randint(100, 2000)
            res = {"number": number}
            await websocket.send(json.dumps(res))
            await asyncio.sleep(1)
    finally:
        connected_clients -= 1  # 클라이언트 연결 해제 시 카운트 감소

async def main():
    async with websockets.serve(handler, "localhost", 8080):
        while True:
            print(f"현재 연결된 클라이언트 수: {connected_clients}")
            await asyncio.sleep(1)

asyncio.run(main())