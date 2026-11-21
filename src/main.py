from xresearch_agent import conduct_research


result = conduct_research(
    "Benefits of artificial intelligence",
    max_results=3
)

print("Research question:", result["question"])
print("Total sources:", result["total_sources"])

for source in result["sources"]:
    print("\nTitle:", source["title"])
    print("URL:", source["url"])
    print("Summary:", source["summary"])