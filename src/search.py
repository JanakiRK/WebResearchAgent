
from ddgs import DDGS


def search_web(query: str, max_results: int = 5) -> list[dict]:
    """
    Search the web and return a list of results.

    Each result contains a title, URL, and snippet.
    """
    if not isinstance(query, str) or not query.strip():
        raise ValueError("Search query cannot be empty.")

    if not isinstance(max_results, int) or isinstance(max_results, bool):
        raise ValueError("max_results must be an integer.")

    if max_results < 1:
        raise ValueError("max_results must be at least 1.")

    try:
        with DDGS() as ddgs:
            results = ddgs.text(
                query.strip(),
                max_results=max_results
            )

            return [
                {
                    "title": result.get("title", ""),
                    "url": result.get("href", ""),
                    "snippet": result.get("body", "")
                }
                for result in results
            ]

    except Exception as error:
        raise RuntimeError(f"Web search failed: {error}") from error
