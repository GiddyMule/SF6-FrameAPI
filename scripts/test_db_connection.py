import os
import sys

# Ensure project root is on sys.path when running directly
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

from app.db import ping_db

if ping_db():
    print("Database connected")
else:
    print("Database NOT connected")
