
import requests
from bs4 import BeautifulSoup


def scrape_webpage(url: str) -> dict:
    """
    Download a webpage and extract its title and text.
    """

    if not url.startswith(("http://", "https://")):
        raise ValueError("URL must start with http:// or https://")

    try:
        response = requests.get(
            url,
            timeout=10,
            headers={"User-Agent": "Mozilla/5.0"}
        )

        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        title = soup.title.get_text(strip=True) if soup.title else ""

        for element in soup(["script", "style", "nav", "footer", "header", "aside"]):
            element.decompose()

        text = " ".join(soup.get_text(separator=" ", strip=True).split())

        return {
            "url": url,
            "title": title,
            "text": text
        }

    except requests.RequestException as error:
        raise RuntimeError(f"Failed to scrape webpage: {error}") from error
