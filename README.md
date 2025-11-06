# 💬 Chat WebSocket (Flask + WebSocket)

Proyek ini adalah aplikasi **chat dua arah real-time** sederhana berbasis **Flask** dan **Flask-Sock (WebSocket).**
Dapat digunakan untuk komunikasi antar perangkat dalam **satu jaringan Wi-Fi (LAN)** atau bahkan diakses secara publik.

---

## 🚀 Fitur

- Komunikasi real-time antar pengguna via WebSocket.
- Notifikasi "user sedang mengetik..."
- Pesan dari server (admin terminal)
- Sistem identitas pengguna (nickname)
- Dapat dijalankan di semua OS: **Linux, Windows, macOS**
- Tidak membutuhkan database.

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

## 🚀 Menjalankan Server

Jalankan perintah berikut di terminal:

```bash
python server_websocket.py
```

Jika berhasil, akan muncul pesan seperti:

```bash
[SERVER] Aktif di port 8080 (HTTPS otomatis)
```

---

## 💻 Menjalankan Aplikasi

Tergantung pada konfigurasi host di baris berikut pada server_websocket.py:

```bash
app.run(host="0.0.0.0", port=8080, debug=False)
```

| Mode | Host | Cara akses | Siapa yang bisa akses |
|----------|----------|----------|----------|
| 🔒 Hanya di komputer sendiri | 127.0.0.1 | http://127.0.0.1:8080 | Hanya komputer lokal |
| 📶 Diakses lewat WiFi lokal | 192.168.x.x (IP lokal PC) | http://192.168.x.x:8080 | Semua perangkat di jaringan WiFi yang sama |
| 🌍 Dapat diakses dari mana saja (tidak disarankan tanpa proteksi) | 0.0.0.0 | tergantung port forwarding router | Semua jaringan yang bisa menjangkau IP publik kamu |

---

## 💡 Catatan:
> 0.0.0.0 artinya server mendengarkan semua IP di komputer kamu.
Aman untuk lokal, selama port 8080 tidak dibuka ke internet oleh router atau layanan seperti ngrok.

---

## 🌐 Mengakses dari HP / Perangkat Lain

1. Pastikan HP dan komputer server terhubung ke WiFi yang sama.  
2. Cek IP komputer kamu:
- Linux/Mac: jalankan ifconfig atau ip addr
- Windows: jalankan ipconfig
3. Lihat IP seperti 192.168.1.10
4. Di HP, buka browser dan ketik:

```bash
http://192.168.1.10:8080
```

---

## 🛡️ Keamanan

- Tidak ada autentikasi → jangan buka ke internet publik tanpa pengamanan.
- Gunakan host="127.0.0.1" jika hanya untuk penggunaan pribadi.
- Gunakan host="192.168.x.x" hanya di jaringan lokal terpercaya.

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
