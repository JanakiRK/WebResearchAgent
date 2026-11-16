
import pytest

from src.search import search_web


def test_empty_query_is_rejected():
    with pytest.raises(ValueError):
        search_web("")


def test_whitespace_query_is_rejected():
    with pytest.raises(ValueError):
        search_web("   ")


def test_invalid_max_results_is_rejected():
    with pytest.raises(ValueError):
        search_web("Python", max_results=0)


def test_non_integer_max_results_is_rejected():
    with pytest.raises(ValueError):
        search_web("Python", max_results="five")
