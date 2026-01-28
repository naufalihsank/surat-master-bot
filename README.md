# 📮 SuratMaster Telegram Bot

Bot Telegram untuk membantu pembuatan **nomor surat otomatis** berdasarkan data yang tersimpan di **Google Sheets**.

Bot ini membatasi akses hanya kepada PIC yang terdaftar dan akan mengisi nomor surat, nama dokumen, serta PIC ke spreadsheet secara otomatis.

---

## 🚀 Fitur Utama

- 🔐 Akses terbatas hanya untuk user tertentu (berdasarkan Telegram ID)
- 📄 Generate nomor surat otomatis
- 📊 Integrasi dengan Google Sheets sebagai database
- 🏷️ Klasifikasi berdasarkan:
  - Jenis surat
  - Kode surat
  - Tanggal
- 🤖 Command interaktif via Telegram

---

## 🧠 Format Nomor Surat

Format yang dihasilkan:

```
<JenisSurat>/<NomorUrut>/<KodeSurat>/T3W-0D0L0000/2025
```

Contoh:

```
C.Tel/001/YN 000/T3W-0D0L0000/2025
```

---

## ⚙️ Requirements

- Python **3.11+**
- Telegram Bot Token
- Google Service Account JSON
- Google Spreadsheet sebagai database

---

## 📦 Install Dependencies

```bash
pip install python-telegram-bot==20.7 gspread pandas oauth2client python-dotenv
```

---

## 🔐 Setup Environment Variable

Buat file `.env`

```env
BOT_TOKEN=ISI_TOKEN_BOT
TARGET_CHAT_ID=-100xxxxxxxxxx
SPREADSHEET_URL=https://docs.google.com/spreadsheets/d/XXXX
GOOGLE_CREDENTIALS_FILE=credentials.json
```

Tambahkan ke `.gitignore`:

```
.env
credentials.json
```

---

## 🔑 Setup Google API

1. Buka **Google Cloud Console**
2. Buat project baru
3. Enable:
   - Google Sheets API
   - Google Drive API
4. Buat **Service Account**
5. Generate **JSON Key**
6. Download → simpan sebagai `credentials.json`
7. Share Google Sheet ke email service account (Editor)

---

## 👤 User yang Diizinkan

User Telegram yang boleh menggunakan bot didefinisikan di:

```python
PIC_NAME = {
    52018198: "SUSI YUNITA"
}
```

Tambahkan Telegram User ID untuk memberi akses.

---

## 🤖 Command Bot

| Command | Fungsi |
|--------|--------|
| `/start` | Memulai bot |
| `/help` | Daftar perintah |
| `/info` | Info format surat |
| `/jenisSurat` | Daftar jenis surat |
| `/kodeSurat` | Daftar kode surat |
| `/buatNomorSurat` | Generate nomor surat |

---

## ✍️ Cara Membuat Nomor Surat

```
/buatNomorSurat <tanggal> <jenis_surat> <kode_surat> <nama_dokumen>
```

Contoh:

```
/buatNomorSurat 21-Januari-2025 internal pelayanan Laporan Tahunan
```

---

## 🗂 Struktur Spreadsheet (Wajib)

| Kolom | Isi |
|------|-----|
| 1 | No |
| 2 | Tanggal |
| 3 | — |
| 4 | Nomor Urut Surat |
| 5 | Nomor Surat (diisi bot) |
| 6 | Nama Dokumen |
| 7 | PIC |

---

## ▶️ Menjalankan Bot

```bash
python surat_master_bot.py
```

Jika berhasil:

```
Bot sedang berjalan...
```

---

## ⚠️ Catatan Penting

- Bot menggunakan **long polling**, tidak perlu server publik
- Jangan pernah publish token atau file credentials
- Pastikan waktu sistem sinkron (JWT Google sensitif waktu)

---

## 🧩 Arsitektur Sistem

```
User Telegram → Bot → Python App → Google Sheets API → Spreadsheet
```

---

## 👨‍💻 Maintainer

SuratMaster Bot — internal automation tool untuk manajemen nomor surat.
