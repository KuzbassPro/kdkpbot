# tests/conftest.py

import os
from pathlib import Path
from dotenv import load_dotenv

def pytest_configure():
    if Path(".env.local").exists():
        load_dotenv(".env.local")
    else:
        load_dotenv()
