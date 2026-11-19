import pytest

from src.scraper import scrape_webpage


def test_empty_url_is_rejected():
    with pytest.raises(ValueError):
        scrape_webpage("")


def test_invalid_url_is_rejected():
    with pytest.raises(ValueError):
        scrape_webpage("www.python.org")


def test_unsupported_protocol_is_rejected():
    with pytest.raises(ValueError):
        scrape_webpage("ftp://example.com")