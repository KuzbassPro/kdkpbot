# src/kdkpbot/db.py

import os
import asyncpg
from dotenv import load_dotenv
from pathlib import Path

if Path(".env.local").exists():
    load_dotenv(".env.local")
else:
    load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

# Соединение будет открываться при старте и использоваться дальше
class Database:
    def __init__(self):
        self.pool = None

    async def connect(self):
        self.pool = await asyncpg.create_pool(DATABASE_URL)

    async def close(self):
        await self.pool.close()

    async def fetch_version(self):
        async with self.pool.acquire() as conn:
            version = await conn.fetchval("SELECT version();")
            return version

# Экземпляр на весь проект
db = Database()
