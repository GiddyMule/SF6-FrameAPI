from pydantic import BaseModel
from typing import List, Optional, Dict

class FrameData(BaseModel):
    startup: Optional[int] = None
    active: Optional[int] = None
    recovery: Optional[int] = None
    on_hit: Optional[int] = None
    on_block: Optional[int] = None

class Move(BaseModel):
    name: str
    command: Optional[str] = None
    frame_data: Optional[FrameData] = None

class Character(BaseModel):
    name: str
    moves: List[Move] = []
