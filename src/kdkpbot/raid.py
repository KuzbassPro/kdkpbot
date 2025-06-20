# src/kdkpbot/raid.py

from dataclasses import dataclass
from typing import List

@dataclass
class Raid:
    date: str
    participants: List[str]
