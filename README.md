# 💬 Chat Dua Arah WebSocket (Python + HTML)

Proyek ini adalah aplikasi **chat dua arah real-time** berbasis **WebSocket** menggunakan Python sebagai server dan HTML/JavaScript sebagai client.  
Dapat digunakan untuk komunikasi antar perangkat dalam **satu jaringan Wi-Fi (LAN)** atau bahkan diakses secara publik menggunakan `ngrok` atau hosting seperti `Render.com`.

---

## 🚀 Fitur

- Komunikasi real-time dua arah antara beberapa client
- Notifikasi "user sedang mengetik..."
- Pesan dari server (admin terminal)
- Sistem identitas pengguna (nickname)
- Dapat dijalankan di semua OS: **Windows, Linux, macOS**

---

## 📦 Persyaratan

- Python 3.8 atau lebih baru
- Browser modern (Chrome, Edge, Firefox, dll)

---

## 🔧 Instalasi

### 1️⃣ Clone repository

```bash
git clone https://github.com/pangeran-droid/Chat-WebSocket.git
cd Chat-WebSocket
```

### 2️⃣ Buat virtual environment (opsional tapi disarankan)

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

### 3️⃣ Install dependensi

```bash
pip install -r requirements.txt
```

---

## ▶️ Menjalankan Server

Jalankan perintah berikut di terminal:

```bash
python server_websocket.py
```

Jika berhasil, akan muncul pesan seperti:

```bash
[SERVER] Aktif di ws://localhost:5000
```

---

## 💻 Menjalankan Client (Browser)

1. Buka file `index.html` di browser.  
2. Jika client berada di perangkat lain (satu jaringan Wi-Fi), ubah URL WebSocket di baris berikut pada `index.html`:

```js
const ws = new WebSocket("ws://192.168.xx.xx:5000");
```

Ganti `192.168.xx.xx` dengan alamat IP komputer yang menjalankan server (`ipconfig` atau `ifconfig`).

---

## 🌐 Akses Publik (Opsional)

Jika ingin diakses dari luar jaringan lokal, gunakan **ngrok** atau hosting seperti **Render.com**.

### 🔹 Dengan ngrok

1. Unduh & instal [ngrok](https://ngrok.com/download)  
2. Jalankan:

```bash
ngrok http 5000
```

3. Salin URL `wss://xxxx.ngrok-free.app` dan ubah pada `index.html`.

### 🔹 Dengan Render.com

1. Push project ini ke GitHub.  
2. Buka [Render.com](https://render.com), login, dan pilih **"New Web Service"**.  
3. Pilih repository ini dan set **Start Command** menjadi:

```bash
python server_websocket.py
```

4. Deploy, dan gunakan URL `wss://...render.com` di `index.html`.

---

## 🧠 Struktur Folder

```
Chat-WebSocket/
│
├── server_websocket.py
├── index.html
├── requirements.txt
└── README.md
```

---

## 📄 LICENSE

Proyek ini bersifat **open-source** di bawah lisensi [MIT License](LICENSE).  
Silakan digunakan untuk belajar, tugas kuliah, atau pengembangan pribadi.
