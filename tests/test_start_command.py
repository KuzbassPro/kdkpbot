# tests/test_start_command.py

import pytest
from unittest.mock import AsyncMock, MagicMock
from kdkpbot.main import start_handler

pytestmark = pytest.mark.asyncio

@pytest.mark.asyncio
async def test_start_handler():
    message = MagicMock()
    message.reply_text = AsyncMock()

    update = MagicMock()
    update.message = message

    context = MagicMock()

    await start_handler(update, context)

    message.reply_text.assert_awaited_once_with("Привет! Бот работает!")
