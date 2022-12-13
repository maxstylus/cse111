from hangman import get_random_word_from
import pytest

mock_list = ["blue", "green", "red", "brown", "black", "white"]

def test_get_random_word_from_returns_a_string():

    #takes in a spelling list returns a random word.
    color = get_random_word_from(mock_list)

    assert isinstance(color, str) == True

def test_random_word_from_returns_contains_no_space():

    # Asserts that the only one word is returned.
    color = get_random_word_from(mock_list)
    assert " " not in color

def test_random_word_from_returns_contains_no_special_chars():
    special_chars = ["-", "_", "!", "&"]
    color = get_random_word_from(mock_list)

    for char in special_chars: 
        assert char not in color
