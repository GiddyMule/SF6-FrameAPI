import sys
from pathlib import Path

# Ensure project root is on sys.path when running directly from scripts/
ROOT_DIR = Path(__file__).resolve().parents[1]
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from app.db import db

characters = db.characters

characters.create_index("name", unique=True)
characters.create_index("versions.patch")

print("Indexes created")
