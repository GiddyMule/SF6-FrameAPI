import sys
from pathlib import Path

# Add parent directory to path so we can import app module
sys.path.insert(0, str(Path(__file__).parent.parent))

from app.services.ingest import ingest_all

if __name__ == "__main__":
    ingest_all()
    print("Ingestion complete.")