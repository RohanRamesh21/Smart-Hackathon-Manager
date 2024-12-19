from flask import Flask, request
from crawl4ai import AsyncWebCrawler, CacheMode
from crawl4ai.extraction_strategy import JsonCssExtractionStrategy
import json
import asyncio

app = Flask(__name__)

schema = {
    "name": "hackathon",
    "baseSelector": ".hackathon-tile",  
    "fields": [
        {"name": "hackathon name", "type": "text"},
        {"name": "Date", "type": "text"},
        {"name": "Prize Money", "type": "text"}
    ]
}

strategy = JsonCssExtractionStrategy(schema)

@app.post('/')
async def handle_post():
    url = request.form["url"]
    async with AsyncWebCrawler(verbose=True) as crawler:
        result = await crawler.arun(url=url, extraction_strategy=strategy)
        products = json.loads(result.extracted_content)
        print(products)
    print(url)
    return "200 ok"

if __name__ == "__main__":
    app.run()
    
