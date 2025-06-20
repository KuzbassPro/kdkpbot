# tests/test_start_command.py

import pytest
from telegram import Update
from telegram.ext import CallbackContext
from kdkpbot.main import start_handler

class FakeMessage:
    def __init__(self):
        self.text = None

    async def reply_text(self, text):
        self.text = text

@pytest.mark.asyncio
async def test_start_handler():
    message = FakeMessage()
    update = Update(update_id=1234, message=message)
    context = CallbackContext(None)

    await start_handler(update, context)

    assert message.text == "Привет! Бот работает!"
