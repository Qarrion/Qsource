# import asyncio
# import websockets

# async def echo(websocket, path):
#     async for message in websocket:
#         print(f"Received message: {message}")

# async def main():
#     async with websockets.serve(echo, "localhost", 8765):
#         await asyncio.Future()  # run forever

# if __name__ == "__main__":
#     asyncio.run(main())

import asyncio
import websockets

async def server(websocket, path):
    # 무한 루프를 통해 연결을 유지합니다.
    while True:
        try:
            # 서버는 클라이언트의 메시지를 기다립니다.
            # 실제 메시지 내용은 이 예제에서는 중요하지 않습니다.
            message = await websocket.recv()
            print(f"Received message: {message}")
            
            # 서버는 일부러 지연을 발생시킵니다.
            # 이 지연은 클라이언트의 타임아웃보다 길게 설정됩니다.
            print("Waiting before sending pong...")
            await asyncio.sleep(3)  # 예: 20초 동안 지연
            print('hello')
            # 실제로는 웹소켓 라이브러리가 자동으로 처리하기 때문에
            # pong 메시지를 수동으로 보낼 필요가 없습니다.
            # 이 코드 라인은 실제로는 실행되지 않습니다.
            # await websocket.pong()

        except websockets.ConnectionClosed:
            print("Connection closed")
            break

start_server = websockets.serve(server, "localhost", 8765)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()