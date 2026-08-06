from pydantic import BaseModel
from fastapi import APIRouter, HTTPException
import httpx, re, asyncio, json

#/api/fetch
fetch = APIRouter(prefix = "/api", tags=["fetch"])

async def hn_fetch(q: str, client: str):

  results = []
  try:
    result = await client.get("https://hn.algolia.com/api/v1/search_by_date?", 
                              params={"query": q, 
                                      "tags": "story",
                                      "hitsPerPage": 5})
    result.raise_for_status()
    body = result.json() #should be awaited 

    platform: str = "Hacker News"
    color: str = '#ff6600'
    snippet: str = ""

    for key in body.get("hits", []):

      item = {
        "platform": platform,
        "color": color,
        "author": key.get("author"),
        "title": key.get("title"),
        "url": key.get("url"),
        "snippet": snippet,
        "score": key.get("points"),
        "meta": f"{key.get('num_comments', 0)} comments",
        "date": key.get("created_at")
      }#still must cover some scenarios
      results.append(item)
    return results
  except httpx.HTTPStatusError as http_err:
    print(f"HTTP error ocurred: {http_err}")

 

async def reddit_fetch(q: str, client: str):

  try:
    result = await client.get("https://www.reddit.com/search.json?",
                            params={
                              "q": q,
                              "sort": "new",
                              "limit": 2,
                              "type": "link,self" #self for self/text posts)
                            },
                            headers={
                              "User-Agent": "python:cadence/1.0 (by /u/Healthy_Watercress)"
                            }
    )
    result.raise_for_status()
    data = result.json()

    return result
  except httpx.HTTPStatusError as http_err:
    print(f"HTTP error ocurred: {http_err}")
    return {}

  #print("STATUS" , result.status_code)
  #print("BODY:" , result.text[:500])#i get html. f@%&orget reddit for now
   

REGISTRY={
    "hn": hn_fetch
    #"reddit": reddit_fetch
}

async def fetch_mentions(q: str, platforms: str):#dict? 

  async with httpx.AsyncClient() as client:
    platform_list = platforms.split(",")
    fetchers = [REGISTRY[n] for n in platform_list if n in REGISTRY]
    #platform = re.search(r'[a-z]+_fetch',str(fetchers[0]))# now only gets 1st

    L = await asyncio.gather(
      *[f(q, client) for f in fetchers]#or map(f, fetchers) map is better for one iterable
    )
    #get item/dict of each list and put into one list
    flat_l_results = [item for sublist in L for item in sublist]  

    return flat_l_results
