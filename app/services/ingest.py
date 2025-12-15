from datetime import datetime
from app.db import db

characters = db["characters"]

PATCH_VERSION = "1.10"   # change when SF6 patches
DATA_SOURCE = "sf6fd"


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

    version = {
        "patch": PATCH_VERSION,
        "scraped_at": datetime.utcnow(),
        "source": DATA_SOURCE,
        "moves": [normalize_move(m) for m in raw_moves],
    }

    characters.update_one(
        {"name": name},
        {
            "$setOnInsert": {"name": name},
            "$push": {"versions": version}
        },
        upsert=True
    )


def ingest_all():
    from sf6fd.scrape import scrape

    data = scrape()
    for character in data:
        ingest_character(character)
