<div align="center">

<img src="https://cdn-icons-png.flaticon.com/512/1380/1380370.png" alt="Chat WebSocket Logo" width="120">

# 💬 Chat WebSocket (Flask + WebSockets)

[![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-Framework-black?style=for-the-badge&logo=flask)](https://flask.palletsprojects.com/)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

**Chat WebSocket** is a simple yet powerful **real-time bi-directional chat application** powered by **Flask** and **Flask-Sock**. It allows devices within the same local network (LAN) to communicate instantly.

</div>

---

## 🚀 Features

- **Real-time Communication** – Instant messaging via WebSockets.
- **Typing Indicators** – "User is typing..." real-time notifications.
- **System Messaging** – Broadcast messages directly from the server terminal to all clients.
- **User Identity** – Simple nickname-based identification system.
- **Cross-Platform** – Runs seamlessly on **Linux, Windows, and macOS**.
- **No Database Required** – Lightweight and ephemeral session-based chat.

---

## Prerequisites

- Python 3.8 or newer.
- Modern Web Browser (Chrome, Edge, Firefox, etc.).

---

## Installation

### 1. Clone the Repository
```bash
git clone [https://github.com/pangeran-droid/Chat-WebSocket.git](https://github.com/pangeran-droid/Chat-WebSocket.git)
cd Chat-WebSocket
```

### 2. Create a Virtual Environment (Recommended)

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Linux/macOS:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

---

## 🚀 Running the Server
Start the server by running:
```bash
python server_websocket.py
```

Upon success, you will see:
```bash
[SERVER] Aktif di port 8080 (HTTPS otomatis)
```

---

## 💻 Access Modes
The access level depends on the `host` configuration in `server_websocket.py`:
```bash
app.run(host="0.0.0.0", port=8080, debug=False)
```

| Mode | Host | Access URL | Visibility |
|----------|----------|----------|----------|
| 🔒 Local Only | 127.0.0.1 | http://127.0.0.1:8080 | Only this computer |
| 📶 Local Network (LAN) | 192.168.x.x | http://[Your-IP]:8080 | All devices on the same Wi-Fi |
| 🌍 Public Access | 0.0.0.0 | Depends on Port Forwarding | Accessible from the internet (Use with caution) |

> [!IMPORTANT]
> **Note on 0.0.0.0:** Setting the host to `0.0.0.0` means the server listens to all available network interfaces on your computer. It is perfectly safe for local development, provided that port `8080` is not exposed to the public internet through router port forwarding or tunneling services like **ngrok**.

---

## 🌐 Mobile / Cross-Device Access
1. Ensure your phone and server are connected to the same Wi-Fi network.
2. Find your computer's local IP address:
    - Linux/Mac: Run ifconfig or ip addr.
    - Windows: Run ipconfig.
3. Locate an IP address like 192.168.1.10.
4. On your mobile browser, enter:

```text
http://192.168.1.10:8080
```

---

## 🛡️ Security Notes
- No Authentication: This version is intended for educational purposes. Do not expose it to the public internet without implementing security layers.
- Private Use: Use host="127.0.0.1" for isolated development.
- Trusted Networks: Use host="0.0.0.0" only within trusted local networks.
---

## Project Structure
```
Chat-WebSocket/
│
├── server_websocket.py
├── index.html
├── requirements.txt
└── README.md
```

---

## LICENSE

**[MIT License](LICENSE)**.  
