# kdkpbot/main.py

from telegram import Update
from telegram.ext import CallbackContext

async def start_handler(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("Привет! Бот работает!")
