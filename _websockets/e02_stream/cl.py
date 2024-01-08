import asyncio
import websockets
import sys
import traceback

args = sys.argv[1:]

import datetime

def now_str():
    now = datetime.datetime.now()
    now_str = now.strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
    return f"[{now_str}] "

# ---------------------------------------------------------------------------- #
#                                  1.Exception                                 #
# ---------------------------------------------------------------------------- #
# 기능적으로 가능하긴하나 코드가 지저분함.
# ---------------------------------------------------------------------------- #
# async def connect():
#     uri = "ws://localhost:6789"
#     #! 두개의 while 문과 두개의 try문이 필요함!
#     try:
#         while True:
#             async with websockets.connect(uri) as websocket:
#                 print('connected')
#                 # cumstom ---------------------------
#                 if len(args)>0:
#                     msg = args[0]
#                 else:
#                     msg = 'hello'
#                 if len(args)>1:
#                     await asyncio.sleep(int(args[1]))
#                 #------------------------------------
#                 print(f">>> client msg send '{msg}'")
#                 await websocket.send(msg)

#                 # async for msg in websocket:
#                 try:
#                     while True:
#                         msg = await websocket.recv()
#                         print(f"{now_str()} <<< client msg recv '{msg}'")

#                 except websockets.exceptions.ConnectionClosed:
#                     print('try reconnect')
#                     continue
                    
#                 except Exception as e:
#                     traceback.format_exc()
#                     print(f"error : {e} '{type(e).__name__}' ")
#     except Exception as e:
#         await asyncio.sleep(10)

# asyncio.run(connect())

# ---------------------------------------------------------------------------- #
#                                  2.Exception                                 #
# ---------------------------------------------------------------------------- #
# https://websockets.readthedocs.io/en/stable/faq/client.html#how-do-i-close-a-connection
# 오피션 reconnect
async def connect():
    uri = "ws://localhost:6789"

    async for websocket in websockets.connect(uri):
        print('connected')
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

        try:
            while True:
                # msg = await websocket.recv()
                msg = await asyncio.wait_for(websocket.recv(),timeout=10)
                print(f"{now_str()} <<< client msg recv '{msg}'")

        except websockets.exceptions.ConnectionClosed:
            print('try reconnect')
            continue
            
        except asyncio.TimeoutError as e:
            print(f"error : {e} '{type(e).__name__}'")
            print("ping")
            try:
                pong = await asyncio.wait_for(websocket.ping(), timeout=20)
                print("pong")
            except:
                continue
            
        except Exception as e:
            # traceback.format_exc()
            print(f"error : {e} '{type(e).__name__}' ")

        # except (asyncio.TimeoutError, websockets.exceptions.ConnectionClosed):
        #     pong = await websocket.ping()
        #     print('hi?')



asyncio.run(connect())