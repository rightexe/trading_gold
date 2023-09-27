import asyncio
import websockets

async def admin_client():
    # Replace 'server_ip_or_hostname' with the actual IP address or hostname of your server
    server_uri = "ws://server_ip_or_hostname:8765"

    async with websockets.connect(server_uri) as websocket:
        while True:
            message = input("Enter a message to send to the server: ")
            await websocket.send(message)

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(admin_client())
