import websockets
import asyncio

port = 7080
print(f"server listening on port {port}")


connected = set()


async def echo(websocket, path):
    print("client connected")

    connected.add(websocket)

    try:
        async for message in websocket:
            print("received message from client: "+message)
            for conn in connected:
                if conn != websocket:
                    await conn.send("someone said: " +message)

    except websockets.exceptions.ConnectionClosed as e:
        print('client disconnected')
    
    finally:
        connected.remove(websocket)


async def main():
    start_server = websockets.serve(echo, 'localhost', port)
    await start_server
    await asyncio.Future() 

asyncio.run(main())
# start_server = websockets.serve(echo, 'localhost', port)
# asyncio.get_event_loop().run_until_complete(start_server)
# asyncio.get_event_loop().run_forever()


# asyncio.run(s)