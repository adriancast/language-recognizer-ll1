from utils import language_recognizer
import pytest

words_that_are_not_from_the_language = [
    'a',
    'b',
    'pi',
    'pff',
]

words_that_are_from_the_language = [
    'pf',
    'pif',
    'psigmhf',
]

@pytest.mark.parametrize("word", words_that_are_not_from_the_language)
def test_word_is_not_from_the_language(word: str) -> bool:
    assert not language_recognizer(word)

@pytest.mark.parametrize("word", words_that_are_from_the_language)
def test_word_is_from_the_language(word: str) -> bool:
    assert language_recognizer(word)

