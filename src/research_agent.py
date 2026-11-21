from search import search_web
from scraper import scrape_webpage
from summariser import summarise_text


def conduct_research(question: str, max_results: int = 5) -> dict:
    """
    Search the web, extract webpage content, and summarise findings.
    """

    if not isinstance(question, str) or not question.strip():
        raise ValueError("Research question cannot be empty.")

    search_results = search_web(question, max_results)

    if not search_results:
        raise RuntimeError("No search results found.")

    research_data = []

    for result in search_results:
        url = result["url"]
        title = result["title"]

        try:
            webpage = scrape_webpage(url)

            summary = summarise_text(webpage["text"])

            research_data.append({
                "title": title,
                "url": url,
                "summary": summary
            })

        except (RuntimeError, ValueError) as error:
            print(f"Skipping {url}: {error}")
            continue

    return {
        "question": question,
        "total_sources": len(research_data),
        "sources": research_data
    }
