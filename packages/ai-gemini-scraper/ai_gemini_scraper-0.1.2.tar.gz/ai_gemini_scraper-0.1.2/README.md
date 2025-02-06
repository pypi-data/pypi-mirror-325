# ai-scraper

A simple package for scraping websites and generating responses using Google's Generative AI.

## Features

- Scrapes a webpage using Selenium with headless Chrome.
- Passes scraped HTML into a Generative AI model along with custom instructions.
- Returns the AI-generated response.

## Installation

You can install the package via pip (after publishing to PyPI):
```
bash
pip install ai-scraper
```
## Usage example
```
from ai_scraper import scrape

response_text = scrape(
    google_api_key="YOUR_GOOGLE_API_KEY",
    url="https://webscraper.io/test-sites/e-commerce/allinone",
    instructions="Return all products names, in JSON."
)
print(response_text)
```