from scraper import scrape_webpage

result = scrape_webpage("https://www.python.org")

print("Page title:", result["title"])
print("\nExtracted text:")
print(result["text"][:500])