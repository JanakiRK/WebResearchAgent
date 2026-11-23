
from research_agent import conduct_research
from report_generator import generate_report


# Conduct research
result = conduct_research(
    "Benefits of artificial intelligence",
    max_results=3
)

# Display research results
print("Research question:", result["question"])
print("Total sources:", result["total_sources"])

for source in result["sources"]:
    print("\nTitle:", source["title"])
    print("URL:", source["url"])
    print("Summary:", source["summary"])

# Generate and save the report
report_path = generate_report(result)

print("\nResearch report saved successfully!")
print("Report location:", report_path)
