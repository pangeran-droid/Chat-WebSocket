import asyncio
import datetime
import json
from flask import Flask, send_from_directory
from flask_sock import Sock

app = Flask(__name__, static_folder=".", static_url_path="")
sock = Sock(app)

connected_clients = set()

@app.route("/")
def index():
    return send_from_directory(".", "index.html")

@sock.route("/ws")
def chat(ws):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(handle_chat(ws))

async def handle_chat(ws):
    connected_clients.add(ws)
    print(f"[{datetime.datetime.now()}] Client baru terhubung. Total: {len(connected_clients)}")

    try:
        while True:
            message = ws.receive()
            if message is None:
                break

            data = json.loads(message)

            if data["type"] == "message":
                name = data.get("name", "Anonim")
                print(f"[{name}] {data['text']}")
                for client in list(connected_clients):
                    if client != ws:
                        await asyncio.to_thread(client.send, json.dumps({
                            "type": "message",
                            "name": name,
                            "text": data["text"]
                        }))

            elif data["type"] in ["typing", "stop_typing"]:
                for client in list(connected_clients):
                    if client != ws:
                        await asyncio.to_thread(client.send, json.dumps({
                            "type": data["type"],
                            "name": data.get("name", "User")
                        }))

    except Exception as e:
        print("[ERROR]", e)
    finally:
        connected_clients.remove(ws)
        print(f"[INFO] Client keluar. Tersisa {len(connected_clients)} client.")


if __name__ == "__main__":
    print("[SERVER] Aktif di port 8080 (HTTPS otomatis)")
    app.run(host="0.0.0.0", port=8080, debug=False)
