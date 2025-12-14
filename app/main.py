from fastapi import FastAPI, HTTPException
from app.db import db, ping_db
from app.models import Character, Move, FrameData
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="SF6 Frame Data API")

# Allow CORS for frontend dashboard if needed
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

characters_collection = db["characters"]

@app.get("/health")
def health_check():
    db_status = "connected" if ping_db() else "disconnected"
    return {"status": "ok", "database": db_status}

@app.get("/characters", response_model=list[Character])
def get_characters():
    docs = list(characters_collection.find({}))
    result = []
    for doc in docs:
        moves = [
            Move(
                name=m.get("name", ""),
                command=m.get("command"),
                frame_data=FrameData(**m.get("frame_data", {}))
            )
            for m in doc.get("moves", [])
        ]
        result.append(Character(name=doc.get("name", ""), moves=moves))
    return result

@app.get("/characters/{name}", response_model=Character)
def get_character(name: str):
    doc = characters_collection.find_one({"name": name})
    if not doc:
        raise HTTPException(status_code=404, detail="Character not found")
    moves = [
        Move(
            name=m.get("name", ""),
            command=m.get("command"),
            frame_data=FrameData(**m.get("frame_data", {}))
        )
        for m in doc.get("moves", [])
    ]
    return Character(name=doc.get("name", ""), moves=moves)
