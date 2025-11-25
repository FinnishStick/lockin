from pydantic import BaseModel

class Source(BaseModel):
    id: str
    name: str
    url: str
    type: str  # rss / html / pdf / api
    enabled: bool = True
