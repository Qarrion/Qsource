import asyncio
import websockets
import json

async def websocket_client():
    async with websockets.connect("ws://localhost:8080") as websocket:
        try:
            while True:
                response = await websocket.recv()
                data = json.loads(response)
                print(data)  # 데이터 처리
        except websockets.exceptions.ConnectionClosed:
            print("Connection closed, attempting to reconnect")
            await websocket_client()  # 재연결 시도

asyncio.run(websocket_client())