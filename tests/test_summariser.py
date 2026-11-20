
import pytest

from src.summariser import summarise_text


def test_summary_returns_first_five_sentences():
    text = (
        "Sentence one. Sentence two. Sentence three. "
        "Sentence four. Sentence five. Sentence six."
    )

    result = summarise_text(text)

    assert result == (
        "Sentence one. Sentence two. Sentence three. "
        "Sentence four. Sentence five."
    )


def test_custom_max_sentences():
    text = "First sentence. Second sentence. Third sentence."

    result = summarise_text(text, max_sentences=2)

    assert result == "First sentence. Second sentence."


def test_empty_text_is_rejected():
    with pytest.raises(ValueError):
        summarise_text("")


def test_invalid_max_sentences_is_rejected():
    with pytest.raises(ValueError):
        summarise_text("Some text.", max_sentences=0)
