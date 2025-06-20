# src/kdkpbot/main.py

import os
import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackContext
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

async def start_handler(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("Привет! Бот работает на локальной машине!")

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start_handler))
    app.run_polling()

if __name__ == "__main__":
    asyncio.run(main())
