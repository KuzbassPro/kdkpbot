# src/kdkpbot/main.py

import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from dotenv import load_dotenv
from pathlib import Path

if Path(".env.local").exists():
    load_dotenv(".env.local")
else:
    load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")

async def start_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Привет! Бот работает!")

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start_handler))
    app.run_polling()

if __name__ == "__main__":
    main()
