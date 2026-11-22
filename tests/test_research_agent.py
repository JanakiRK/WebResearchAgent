
import pytest
from unittest.mock import patch
from research_agent import conduct_research



def test_empty_question_is_rejected():
    with pytest.raises(ValueError):
        conduct_research("")


@patch("research_agent.search_web")
def test_no_search_results_are_handled(mock_search):
    mock_search.return_value = []

    with pytest.raises(RuntimeError):
        conduct_research("Artificial Intelligence")


@patch("research_agent.scrape_webpage")
@patch("research_agent.search_web")
def test_research_workflow(mock_search, mock_scrape):
    mock_search.return_value = [
        {
            "title": "Example Article",
            "url": "https://example.com"
        }
    ]

    mock_scrape.return_value = {
        "title": "Example Article",
        "url": "https://example.com",
        "text": "Python is popular. Python is easy to learn."
    }

    result = conduct_research("Python", max_results=1)

    assert result["question"] == "Python"
    assert result["total_sources"] == 1
    assert len(result["sources"]) == 1
    assert result["sources"][0]["title"] == "Example Article"


@patch("research_agent.scrape_webpage")
@patch("research_agent.search_web")
def test_failed_webpage_is_skipped(mock_search, mock_scrape):
    mock_search.return_value = [
        {
            "title": "Unavailable Article",
            "url": "https://example.com"
        }
    ]

    mock_scrape.side_effect = RuntimeError("Download failed")

    result = conduct_research("Python", max_results=1)

    assert result["total_sources"] == 0
    assert result["sources"] == []
