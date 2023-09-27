from fastapi import FastAPI, WebSocket
from typing import Set

app = FastAPI()

# Maintain a set of connected WebSocket clients
connected_clients: Set[WebSocket] = set()


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
  await websocket.accept()
  connected_clients.add(websocket)

  try:
    while True:
      message = await websocket.receive_text()
      # Broadcast the received message to all connected clients
      for client in connected_clients:
        await client.send_text(message)
  except WebSocketDisconnect:
    connected_clients.remove(websocket)
