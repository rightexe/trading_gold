import asyncio
import websockets


async def client():
    # Replace 'server_ip_or_hostname' with the actual IP address or hostname of your server
    server_uri = "ws://server_ip_or_hostname:8765"

    async with websockets.connect(server_uri) as websocket:
        while True:
            message = await websocket.recv()
            print("Received:", message)

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(client())
