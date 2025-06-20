# tests/test_raid.py

from kdkpbot.raid import Raid

def test_raid_creation():
    raid = Raid(date="2024-06-01", participants=["Player1", "Player2"])
    assert raid.date == "2024-06-01"
    assert raid.participants == ["Player1", "Player2"]
