import feedparser
from datetime import datetime
from typing import List, Dict

MSB_RSS_URL = "https://www.msb.se/RSS/nyheter/"

def parse_date(raw_date: str) -> datetime:
    try:
        return datetime(*raw_date[:6])
    except:
        return datetime.utcnow()

def fetch_msb_feed() -> List[Dict]:
    feed = feedparser.parse(MSB_RSS_URL)
    items = []

    for entry in feed.entries:
        item = {
            "source": "MSB",
            "title": entry.get("title"),
            "summary": entry.get("summary"),
            "link": entry.get("link"),
            "published": parse_date(entry.get("published_parsed")),
            "raw": entry
        }
        items.append(item)

    return items

if __name__ == "__main__":
    data = fetch_msb_feed()
    for d in data[:3]:
        print(d["title"], d["published"])
