import asyncio
import websockets
import datetime
import json

connected_clients = set()

async def chat_handler(websocket):
    connected_clients.add(websocket)
    print(f"[{datetime.datetime.now()}] Client baru terhubung. Total client: {len(connected_clients)}")

    try:
        async for message in websocket:
            data = json.loads(message)
            if data["type"] == "message":
                name = data.get("name", "Anonim")
                print(f"[{name}] {data['text']}")
                for client in connected_clients:
                    if client != websocket:
                        await client.send(json.dumps({
                            "type": "message",
                            "name": name,
                            "text": data["text"]
                        }))
            elif data["type"] == "typing":
                for client in connected_clients:
                    if client != websocket:
                        await client.send(json.dumps({
                            "type": "typing",
                            "name": data.get("name", "User")
                        }))
            elif data["type"] == "stop_typing":
                for client in connected_clients:
                    if client != websocket:
                        await client.send(json.dumps({
                            "type": "stop_typing",
                            "name": data.get("name", "User")
                        }))

    except websockets.exceptions.ConnectionClosed:
        print("[INFO] Client terputus.")
    finally:
        connected_clients.remove(websocket)
        print(f"[INFO] Client keluar. Tersisa {len(connected_clients)} client.")


async def send_from_server():
    while True:
        msg = await asyncio.to_thread(input, "[Server] Ketik pesan: ")
        if msg.strip():
            for client in connected_clients:
                try:
                    await client.send(json.dumps({
                        "type": "message",
                        "name": "Server",
                        "text": msg
                    }))
                except:
                    pass

async def main():
    async with websockets.serve(chat_handler, "0.0.0.0", 5000):
        print("[SERVER] Aktif di ws://localhost:5000")
        await asyncio.gather(send_from_server(), asyncio.Future())

if __name__ == "__main__":
    asyncio.run(main())
