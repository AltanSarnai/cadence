from pydantic import BaseModel
from fastapi import APIRouter
from app.services.anthropic_client import monitor
from app.services.fetch import fetch_mentions
from typing import Optional

#/api/monitor
router = APIRouter(prefix = "/api", tags=["monitor"])

class ItemModel(BaseModel):
   
    platform: str #= "hn"
    color: str
    title: str 
    snippet: str
    author: str
    score: int
    meta: str
    date: str
    url: Optional[str] = None

class MonitorResponse(BaseModel):#, arg1, arg2):
    results: list[ItemModel] 
    total: int

#fetch('/api/monitor?q=' + encodeURIComponent(q) + '&platforms=' + platforms.join(','))
@router.get("/monitor", response_model=MonitorResponse)
async def fetch_data(
    q: str = "Marketing with AI", 
    platforms: str = "hn"): 

    results = await fetch_mentions( q, platforms)
    total: int 

    return MonitorResponse(results = results, total= len(results))
