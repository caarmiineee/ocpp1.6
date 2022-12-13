
import asyncio
import websockets

async def echo(websocket):
    async for message in websocket:
        print('send message')
        if message == 'chiudi':
            break
        await websocket.send(message)

async def main():
    async with websockets.serve(echo, "localhost", 8765):
        print('websockets connect')
        await asyncio.Future()  # run forever

asyncio.run(main())