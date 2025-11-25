from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel, Field


class Threat(BaseModel):        
    id: str = Field(..., alias="_id")  # använder hash som _id
    source: str
    title: str
    summary: Optional[str]
    link: str
    published: datetime
    category: Optional[str] = None
    tags: List[str] = []
    hash: str  # used to detect duplicates
    raw: dict  # full unprocessed data from collector
