import os
import asyncio
import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
    CallbackContext,
)
from dotenv import load_dotenv

load_dotenv()
CHAT_ID = os.getenv("TARGET_CHAT_ID")

# Ganti dengan token bot Telegram Anda
TELEGRAM_BOT_TOKEN = os.getenv("BOT_TOKEN")

# Setup Google Sheets API
SHEET_URL = os.getenv("SPREADSHEET_URL")  # Ganti dengan URL Google Sheets Anda
CREDENTIALS_FILE = os.getenv("GOOGLE_CREDENTIALS_FILE")  # Ganti dengan path ke file kredensial

PIC_NAME = {
    52018198: "SUSI YUNITA",
    390264618: "KHANAYA",
    2098381506: "YOGA JULIAN",
    281589378: "IHSAN NAUFAL",
    49400179: "AM HERMAYANI",
    1141645339: "AM SOMA",
    72575696: "AM AYU RASMINI",
    43151962: "AM IRMA",
    76623734: "AM NITYA",
    468714589: "AM YOGI",
    1993277434: "SARI",
    1192100482: "VEMY",
    291730177: "WINDA",
    1317309156: "MAYUN",
    1494465082: "DIAN",
}
# Inisialisasi Google Sheets API
scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive",
]
creds = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE, scope)
client = gspread.authorize(creds)
sheet = client.open_by_url(
    SHEET_URL
).sheet1  # Ganti `sheet1` dengan nama sheet yang sesuai

# Mapping jenis surat
JENIS_SURAT = {"internal": "C.Tel", "eksternal": "Tel", "kontrak": "K.Tel"}

KODE_SURAT = {"umum": "UM 000", "pelayanan": "YN 000", "kontrak": "HK.820"}


def format_tanggal(tanggal: str) -> str:
    """Menghilangkan tanda '-' pada tanggal."""
    return tanggal.replace("-", " ")


async def start(update: Update, context: CallbackContext) -> None:
    user_id = update.effective_user.id

    if user_id not in PIC_NAME:
        await update.message.reply_text(
            "❌ Maaf, Anda tidak memiliki akses untuk membuat nomor surat."
        )
        return
    """Menjalankan perintah /start"""
    await update.message.reply_text(
        "Halo! Saya bot pengelola surat.\nGunakan /buatNomorSurat untuk membuat nomor surat."
    )


async def help_command(update: Update, context: CallbackContext) -> None:
    user_id = update.effective_user.id

    if user_id not in PIC_NAME:
        await update.message.reply_text(
            "❌ Maaf, Anda tidak memiliki akses untuk membuat nomor surat."
        )
        return

    """Menjalankan perintah /help"""
    await update.message.reply_text(
        "Perintah yang tersedia:\n"
        "/start - Memulai bot\n"
        "/help - Menampilkan bantuan\n"
        "/info - Menampilkan informasi Bot\n"
        "/buatNomorSurat - Membuat nomor surat\n"
        "/jenisSurat - Melihat jenis surat\n"
        "/kodeSurat - Melihat kode surat"
    )


async def info_command(update: Update, context: CallbackContext) -> None:
    user_id = update.effective_user.id

    if user_id not in PIC_NAME:
        await update.message.reply_text(
            "❌ Maaf, Anda tidak memiliki akses untuk membuat nomor surat."
        )
        return

    """Menjalankan perintah /help"""
    await update.message.reply_text(
        "Takah yang dibuatkan oleh SuratMaster Bot adalah berdasarkan jenis surat, kode surat, dan nomor surat yang tersedia pada google docs\n\n"
        "=======================\n"
        "**JENIS SURAT**\n"
        "=======================\n"
        "`<internal>`\tInternal	C.Tel ....../kode jenis surat/T3W--0D0L0000/2025  \n"
        "`<eksternal>`\t Eksternal	Tel ....../kode jenis surat/T3W--0D0L0000/2025 \n"
        "`<kontrak>`\t Kontrak	K.Tel ....../kode jenis surat/T3W--0D0L0000/2025 \n\n"
        "=======================\n"
        "**KODE SURAT**\n"
        "=======================\n"
        "`<umum>`\t\tUM 000 UMUM \n"
        "`<pelayanan>`\tYN 000 PELAYANAN JASA/FASILITAS TELEKOMUNIKASI \n"
        "`<kontrak>`\tHK.820 AMANDEMEN KONTRAK/PKS \n"
        "=======================\n\n"
        "Jenis surat ini akan berpengaruh pada takah yang dihasilkan, jadi silahkan pilih sesuai kebutuhan 😁",
        parse_mode="Markdown",
    )


async def jenis_surat(update: Update, context: CallbackContext) -> None:
    user_id = update.effective_user.id

    if user_id not in PIC_NAME:
        await update.message.reply_text(
            "❌ Maaf, Anda tidak memiliki akses untuk membuat nomor surat."
        )
        return

    """Menjalankan perintah /jenis_surat"""
    await update.message.reply_text(
        "=======================\n"
        "**JENIS SURAT**\n"
        "=======================\n"
        "`<internal>`\tInternal	C.Tel ....../kode jenis surat/T3W--0D0L0000/2025  \n"
        "`<eksternal>`\t Eksternal	Tel ....../kode jenis surat/T3W--0D0L0000/2025 \n"
        "`<kontrak>`\t Kontrak	K.Tel ....../kode jenis surat/T3W--0D0L0000/2025 \n\n"
        "=======================\n"
        "Jenis surat ini akan berpengaruh pada takah yang dihasilkan, jadi silahkan pilih sesuai kebutuhan 😁",
        parse_mode="Markdown",
    )


async def kode_surat(update: Update, context: CallbackContext) -> None:
    user_id = update.effective_user.id

    if user_id not in PIC_NAME:
        await update.message.reply_text(
            "❌ Maaf, Anda tidak memiliki akses untuk membuat nomor surat."
        )
        return

    """Menjalankan perintah /jenis_surat"""
    await update.message.reply_text(
        "**KODE SURAT**\n"
        "=======================\n"
        "`<umum>`\t\tUM 000 UMUM \n"
        "`<pelayanan>`\tYN 000 PELAYANAN JASA/FASILITAS TELEKOMUNIKASI \n"
        "`<kontrak>`\tHK.820 AMANDEMEN KONTRAK/PKS \n"
        "Kode surat ini akan berpengaruh pada takah yang dihasilkan, jadi silahkan pilih sesuai kebutuhan 😁",
        parse_mode="Markdown",
    )


async def buat_nomor_surat(update: Update, context: CallbackContext) -> None:
    user_id = update.effective_user.id
    pic_name = PIC_NAME.get(user_id)
    print("PIC NAME: ", pic_name)
    if user_id not in PIC_NAME:
        await update.message.reply_text(
            "❌ Maaf, Anda tidak memiliki akses untuk membuat nomor surat."
        )
        return

    if len(context.args) < 4:
        await update.message.reply_text(
            "Gunakan format: \n"
            "`/buatNomorSurat <tanggal> <jenis_surat> <kode_surat> <nama_dokumen>`\n\n"
            "Contoh: /buatNomorSurat 21-Januari-2025 internal pelayanan Laporan Tahunan\n\n"
            "==================\n"
            "format tanggal harus menggunakan tanda '-' untuk memisahkan tanggal, bulan, dan tahun\n"
            "==================\n"
            "Jika masih bingung silahkan `/help` untuk melihat informasi lebih detail",
            parse_mode="Markdown",
        )
        return

    tanggal_input, jenis_surat_input, kode_surat_input, *nama_dokumen_input = (
        context.args
    )
    tanggal_format = format_tanggal(tanggal_input)
    nama_dokumen = " ".join(nama_dokumen_input)

    jenis_surat = JENIS_SURAT.get(jenis_surat_input.lower())
    kode_surat = KODE_SURAT.get(kode_surat_input.lower())
    if not jenis_surat or not kode_surat:
        await update.message.reply_text("Jenis surat atau kode surat tidak valid.")
        return

    data = sheet.get_all_values()
    df = pd.DataFrame(data)

    if df.empty:
        await update.message.reply_text("Google Sheet kosong atau tidak dapat diakses.")
        return

    last_date = None
    for index, row in df.iterrows():
        if row[1]:
            last_date = row[1]
        else:
            df.at[index, 1] = last_date

    df_filtered = df[df[1] == tanggal_format]
    if df_filtered.empty:
        await update.message.reply_text(
            f"Tidak ditemukan entri untuk tanggal {tanggal_format}."
        )
        return

    for index in df_filtered.index:
        if df.at[index, 4] == "":
            nomor_surat = df.at[index, 3]
            takah = f"{jenis_surat}/{nomor_surat}/{kode_surat}/T3W-0D0L0000/2025"

            sheet.update_cell(index + 1, 5, takah)
            sheet.update_cell(index + 1, 6, nama_dokumen)
            sheet.update_cell(index + 1, 7, pic_name)

            await update.message.reply_text(
                f"✅ Nomor surat berhasil dibuat:\n"
                f"📌 **Nomor Surat:** `{takah}`\n"
                f"📄 **Nama Dokumen:** `{nama_dokumen}`",
                parse_mode="Markdown",
            )
            return

    await update.message.reply_text(
        f"Tidak ada slot kosong di tanggal {tanggal_format}."
    )


def main():
    """Menjalankan bot"""
    app = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

    # Menambahkan handler untuk perintah
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("info", info_command))
    app.add_handler(CommandHandler("buatNomorSurat", buat_nomor_surat))
    app.add_handler(CommandHandler("jenisSurat", jenis_surat))
    app.add_handler(CommandHandler("kodeSurat", kode_surat))

    # Menjalankan bot
    print("Bot sedang berjalan...")
    app.run_polling()


if __name__ == "__main__":
    main()
