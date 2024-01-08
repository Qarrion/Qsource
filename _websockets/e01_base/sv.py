import asyncio
import websockets
import traceback
# ---------------------------------------------------------------------------- #
#                                    1. base                                   #
# ---------------------------------------------------------------------------- #
# 간단하게 websocket에서 msg를 받아 다시 보내는 웹소켓
# ---------------------------------------------------------------------------- #

# async def conn_handler(websocket,path):
#     async for msg in websocket:
#         print(f"<<< server msg recv '{msg}'")
#         print(f">>> server msg send '{msg}'")
#         await websocket.send(msg+' sv')

# start_server = websockets.serve(conn_handler, "localhost", 6789)
# asyncio.get_event_loop().run_until_complete(start_server)
# asyncio.get_event_loop().run_forever()

# ---------------------------------------------------------------------------- #
#                                    2.loop                                    #
# ---------------------------------------------------------------------------- #
# async with를 이용하여 websocket.serve 웹소켓 서버를 실행
# 서버는 'localhost'에 접속하는 client에 대하여 conn_handler 실행
# await asyncio.Future() 는 서버가 실행되고 난 후에도 다음 클라이언트 대기
# ---------------------------------------------------------------------------- #

# async def conn_handler(websocket,path):
#     print(f"client {websocket.remote_address} connected")
#     async for msg in websocket:
#         print(f"<<< server msg recv '{msg}'")
#         print(f">>> server msg send '{msg}'")
#         await websocket.send(msg+' sv')

# async def main():
#     async with websockets.serve(conn_handler, "localhost", 6789):
#         await asyncio.Future()

# if __name__ == "__main__":
#     asyncio.run(main())

# ---------------------------------------------------------------------------- #
#                                    3.While                                   #
# ---------------------------------------------------------------------------- #
# while 루프를 사용할경우 좀더 낮은 레벨에서 컨드롤 가능 함.

async def conn_handler(websocket,path):
    # async for msg in websocket:
    client = websocket.remote_address
    print(f"client '{client}' connected")
    try:
        while True:
            msg = await websocket.recv()
            print(f"<<< server msg recv '{msg}'")
            print(f">>> server msg send '{msg}'")
            
            await websocket.send(msg+' sv')

    except websockets.exceptions.ConnectionClosed as e:
        print(f"client '{client}' disconnected. with exceptions: {e}")

    except Exception as e:
        traceback.format_exc()

async def main():
    async with websockets.serve(conn_handler, "localhost", 6789):
        await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())

# import asyncio
# import websockets

# async def receive_specific_message(websocket, path):
#     while True:
#         message = await websocket.recv()
#         print(f"Received message: {message}")

#         # 특정 조건을 만족하는 메시지가 도착하면 처리하고 루프를 종료
#         if message == "특정 조건":
#             print("특정 조건의 메시지를 받았습니다.")
#             break  # 루프 종료

# start_server = websockets.serve(receive_specific_message, "localhost", 6789)
# asyncio.get_event_loop().run_until_complete(start_server)
# asyncio.get_event_loop().run_forever()