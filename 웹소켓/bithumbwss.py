import websockets
import asyncio
import json

async def bithumb_ws_client():
    uri = "wss://pubwss.bithumb.com/pub/ws"
    async with websockets.connect(uri, ping_interval=None) as websocket: # ping_interval=None: disable ping which is used to keep connection alive
        greeting = await websocket.recv() # receive message from server
        print(f"< {greeting}")

    subscribe_fmt = {
        "type": "ticker",
        "symbols": ["BTC_KRW"],
        "tickTypes": ["1H"]
    }
    subscribe_data = json.dumps(subscribe_fmt)
    await websocket.send(subscribe_data)

    while True:
        data = await websocket.recv()
        data = json.loads(data)
        print(data)

if __name__ == "__main__":
    asyncio.run(bithumb_ws_client())