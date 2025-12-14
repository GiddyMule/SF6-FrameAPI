from datetime import datetime
from app.db import db

characters = db["characters"]

def normalize_move(move: dict) -> dict:
    return {
        "name": move.get("name"),
        "command": move.get("input"),
        "frame_data": {
            "startup": move.get("startup"),
            "active": move.get("active"),
            "recovery": move.get("recovery"),
            "on_hit": move.get("onHit"),
            "on_block": move.get("onBlock"),
        }
    }

def ingest_character(character: dict):
    name = character.get("name") or character.get("character")
    raw_moves = character.get("moves", [])

    document = {
        "name": name,
        "moves": [normalize_move(m) for m in raw_moves],  # will be empty for stub
        "last_updated": datetime.utcnow()
    }

    characters.update_one(
        {"name": name},
        {"$set": document},
        upsert=True
    )

def ingest_all():
    from sf6fd.scrape import scrape

    data = scrape()
    for character in data:
        ingest_character(character)
