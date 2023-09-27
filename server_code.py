import asyncio
import websockets

# Maintain a list of connected clients
clients = set()

async def server(websocket, path):
    # Add the connected client to the list
    clients.add(websocket)
    try:
        async for message in websocket:
            # Broadcast the received message to all connected clients
            for client in clients:
                await client.send(message)
    except websockets.exceptions.ConnectionClosedError:
        pass
    finally:
        # Remove the client when they disconnect
        clients.remove(websocket)

if __name__ == "__main__":
    # Replace '0.0.0.0' with your server's IP address or hostname
    server_host = '0.0.0.0'
    server_port = 8765

    start_server = websockets.serve(server, server_host, server_port)

    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()
