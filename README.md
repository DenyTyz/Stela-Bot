<div align="center">

```
███████╗██╗   ██╗██████╗  ██████╗ ██╗  ██╗
╚══███╔╝╚██╗ ██╔╝██╔══██╗██╔═══██╗╚██╗██╔╝
  ███╔╝  ╚████╔╝ ██████╔╝██║   ██║ ╚███╔╝ 
 ███╔╝    ╚██╔╝  ██╔══██╗██║   ██║ ██╔██╗ 
███████╗   ██║   ██║  ██║╚██████╔╝██╔╝ ██╗
╚══════╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝
```

<h3>Panduan Instalasi Lengkap Bot Stela & Dashboard Next.js</h3>

<a href="https://nexiohost.in"><img src="https://img.shields.io/badge/⭐%20PREMIUM%20HOSTING-NexioHost-FFD700?style=for-the-badge&labelColor=1a1a2e&color=FFD700&logoColor=FFD700"/></a>

<p>
  <a href="https://python.org"><img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white"/></a>
  <a href="https://nodejs.org/"><img src="https://img.shields.io/badge/Node.js-18+-339933?style=for-the-badge&logo=node.js&logoColor=white"/></a>
  <a href="https://nextjs.org"><img src="https://img.shields.io/badge/Next.js-14+-000000?style=for-the-badge&logo=nextdotjs&logoColor=white"/></a>
  <a href="https://discordpy.readthedocs.io"><img src="https://img.shields.io/badge/Discord.py-v2-5865F2?style=for-the-badge&logo=discord&logoColor=white"/></a>
</p>
<p>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-red?style=for-the-badge"/></a>
  <a href="https://discord.gg/steladev"><img src="https://img.shields.io/badge/Discord-Join_Server-5865F2?style=for-the-badge&logo=discord&logoColor=white"/></a>
</p>

</div>

---

Selamat datang di panduan instalasi **Stela**. Panduan ini dibuat khusus untuk pemula, menjelaskan langkah demi langkah dari nol hingga bot dan dashboard Anda menyala dengan sempurna.

---

## ✦ Tahap 1: Prasyarat (Aplikasi yang Dibutuhkan)

Sebelum mulai, pastikan Anda sudah menginstal aplikasi berikut di komputer Anda:

1. **Python (Minimal versi 3.10)**
   - Unduh dari [python.org](https://www.python.org/downloads/).
   - ⚠️ **SANGAT PENTING**: Saat menginstal, pastikan Anda MENCENTANG kotak **"Add Python to PATH"** di bagian bawah installer.

2. **Node.js (Minimal versi 18)**
   - Unduh versi LTS dari [nodejs.org](https://nodejs.org/).
   - Instal seperti biasa (tinggal klik Next).

3. **Visual Studio Code (Rekomendasi Editor)**
   - Unduh dari [code.visualstudio.com](https://code.visualstudio.com/).

4. **Akun Cloudflare (Gratis)**
   - Daftar di [cloudflare.com](https://dash.cloudflare.com/sign-up) (Dibutuhkan untuk membuat tunnel HTTPS gratis bagi API Dashboard).

---

## ✦ Tahap 2: Persiapan Discord Developer Portal

Anda memerlukan Token Bot dan Client Secret dari Discord agar bot dan dashboard bisa terhubung.

1. Buka [Discord Developer Portal](https://discord.com/developers/applications).
2. Klik tombol **"New Application"** di kanan atas, beri nama **Stela** (atau nama bot Anda).
3. Buka menu **Bot** di panel kiri:
   - Gulir ke bawah ke bagian **Privileged Gateway Intents**.
   - Aktifkan ketiga tombol: **Presence Intent**, **Server Members Intent**, dan **Message Content Intent**.
   - Klik **Reset Token**, lalu **Salin (Copy) Token** tersebut (simpan di tempat yang aman).
4. Buka menu **OAuth2** -> **General** di panel kiri:
   - Salin **Client ID**.
   - Klik **Reset Secret**, lalu salin **Client Secret**.
5. Buka menu **OAuth2** -> **URL Generator**:
   - Centang **bot** dan **applications.commands**.
   - Di bagian permissions, centang **Administrator**.
   - Salin URL yang muncul dan buka di browser untuk memasukkan bot ke server Discord Anda.

---

## ✦ Tahap 3: Instalasi & Menjalankan Bot

Sekarang kita akan menyalakan bot-nya terlebih dahulu.

1. Buka folder `Stela` menggunakan VS Code.
2. Buka terminal baru di VS Code (Klik menu `Terminal` > `New Terminal`).
3. Masuk ke folder bot dengan mengetik:
   ```bash
   cd bot
   ```
4. Buat dan aktifkan Virtual Environment (agar library tidak berantakan):
   ```bash
   python -m venv .venv
   .\.venv\Scripts\activate   # (Untuk pengguna Windows)
   ```
   *(Jika Anda menggunakan Mac/Linux: `source .venv/bin/activate`)*
5. Instal semua kebutuhan bot:
   ```bash
   pip install -r requirements.txt
   ```
6. **Konfigurasi Lingkungan:**
   - Di dalam folder `bot`, cari file bernama `.env.example`.
   - Ganti (rename) nama file tersebut menjadi `.env`.
   - Buka file `.env` dan isikan data Anda, contoh:
     ```env
     TOKEN              = "TOKEN_BOT_ANDA_DI_SINI"
     brand_name         = 'Stela'
     OWNER_IDS          = ID_DISCORD_ANDA_DISINI
     
     # Biarkan API dan Tunnel menyala
     API_ENABLED        = "true"
     API_PORT           = "8000"
     DASHBOARD_API_KEY  = "buat_password_rahasia_anda_disini"
     TUNNEL_ENABLED     = "true"
     ```
7. Jalankan Bot:
   ```bash
   python Stela.py
   ```
   *Tunggu hingga terminal menampilkan `Loaded & Online!`. Bot Anda sekarang hidup!*

---

## ✦ Tahap 4: Setup Cloudflare Tunnel (Untuk Dashboard API)

Agar Dashboard (Next.js) bisa berkomunikasi dengan Bot (Python) secara aman dari luar, kita butuh jembatan (Tunnel) HTTPS. Bot sudah memiliki sistem otomatis, Anda hanya perlu mengaturnya di website Cloudflare:

1. Pergi ke [Cloudflare Zero Trust](https://one.dash.cloudflare.com/) -> **Networks** -> **Tunnels**.
2. Klik **Create a tunnel**, pilih **Cloudflared**.
3. Beri nama tunnel-nya (misal: `stela-api`), klik Save.
4. Di bagian *Install connector*, Anda akan melihat kotak kode yang panjang. Cari tulisan `eyJh...` (itu adalah Token Anda). **Salin Token tersebut**.
5. Buka tab **Public Hostname** (di halaman yang sama), klik **Add a public hostname**:
   - **Subdomain:** (Isi bebas, misal: `api-stela`)
   - **Domain:** (Pilih domain Anda jika punya, atau gunakan domain gratisan yang Anda miliki di Cloudflare)
   - **Service Type:** `HTTP`
   - **URL:** `localhost:8000`
   - Klik **Save**.
6. Kembali ke VS Code, buka file `.env` di folder `bot`, dan tambahkan:
   ```env
   CF_TUNNEL_TOKEN = "TOKEN_YANG_ANDA_SALIN_TADI"
   CF_TUNNEL_URL   = "https://api-stela.domainanda.com"
   ```
7. Matikan bot di terminal (tekan `Ctrl + C`), lalu jalankan lagi `python Stela.py`. Tunnel akan otomatis menyala!

---

## ✦ Tahap 5: Instalasi & Menjalankan Dashboard

1. Buka tab terminal baru di VS Code.
2. Masuk ke folder dashboard:
   ```bash
   cd dashboard
   ```
3. Instal dependencies Node.js:
   ```bash
   npm install
   ```
4. **Konfigurasi Lingkungan:**
   - Cari file `.env.example` di dalam folder `dashboard`, ubah namanya menjadi `.env.local`.
   - Buka file `.env.local` dan isikan:
     ```env
     NEXT_PUBLIC_API_URL           = "https://api-stela.domainanda.com/api/v1"  # Sesuai URL Cloudflare Anda
     NEXT_PUBLIC_DASHBOARD_API_KEY = "password_rahasia_yang_sama_dengan_bot"
     
     NEXTAUTH_URL                  = "http://localhost:3000"
     NEXTAUTH_SECRET               = "tulis_teks_acak_yang_panjang_disini"
     
     DISCORD_CLIENT_ID             = "CLIENT_ID_DARI_TAHAP_2"
     DISCORD_CLIENT_SECRET         = "CLIENT_SECRET_DARI_TAHAP_2"
     
     NEXT_PUBLIC_ADMIN_IDS         = "ID_DISCORD_ANDA"
     NEXT_PUBLIC_BRAND_NAME        = "Stela"
     NEXT_PUBLIC_BRAND_NAME_WORD   = "ST"
     ```
5. **Tambahkan Redirect URI di Discord Portal:**
   - Buka lagi [Discord Developer Portal](https://discord.com/developers/applications).
   - Masuk ke menu **OAuth2** -> **General**.
   - Di bagian Redirects, klik **Add Redirect** dan masukkan: `http://localhost:3000/api/auth/callback/discord`
   - Simpan perubahan (Save Changes).
6. Jalankan Dashboard:
   ```bash
   npm run dev
   ```
7. Buka browser Anda dan kunjungi `http://localhost:3000`. Dashboard Stela Anda sekarang sudah bisa diakses!

---

## ✦ Troubleshooting & FAQ

- **Bot tidak mau menyala?**
  Pastikan Anda telah mengaktifkan 3 buah *Gateway Intents* di Discord Developer Portal (seperti di Tahap 2).
- **Dashboard tidak bisa Login (Error)?**
  Pastikan *Client ID*, *Client Secret*, dan *Redirect URI* di portal Discord sudah sesuai persis dengan yang ada di file `.env.local`.
- **Dashboard mengatakan API Offline?**
  Pastikan bot menyala (`python Stela.py`), pastikan Cloudflare Tunnel terhubung, dan URL API sudah persis sama.

<div align="center">

© 2026 Stela Devs — MIT License

</div>
