"""Verify that the prefix and suffix functions work correctly."""

from words import prefix, suffix
import pytest


def test_prefix():
    """Verify that the prefix function works correctly.
    Parameters: none
    Return: nothing
    """
    # Call the prefix function and verify that it returns a string.
    pre = prefix("upbeat", "upgrade")
    assert isinstance(pre, str), "prefix function must return a string"

    # Call the prefix function ten times and use an assert
    # statement to verify that the string returned by the
    # prefix function is correct each time.
    assert prefix("cat", "catalog") == "cat"
    assert prefix("", "") == ""
    assert prefix("", "correct") == ""
    assert prefix("clear", "") == ""
    assert prefix("happy", "funny") == ""
    assert prefix("cat", "catalog") == "cat"
    assert prefix("dogmatic", "dog") == "dog"
    assert prefix("jump", "joyous") == "j"
    assert prefix("upbeat", "upgrade") == "up"
    assert prefix("Disable", "dIstasteful") == "dis"

def test_suffix():

    # Call the prefix function and verify that it returns a string.
    suf = suffix("lunacy", "democracy")
    assert isinstance(suf, str), "prefix function must return a string"

    assert suffix("denial", "trial") == "ial"
    assert suffix("Denial", "TRIAL") == "ial"
    assert suffix("nuisance", "tolerance") == "ance"
    assert suffix("clear", "fear") == "ear"
    assert suffix("bunny", "funny") == "unny"
    assert suffix("dialog", "catalog") == "alog"
    assert suffix("dogmatic", "pragmatic") == "gmatic"
    assert suffix("frivalous", "joyous") == "ous"
    assert suffix("downgrade", "upgrade") == "grade"
    assert suffix("Disable", "incredible") == "ble"


# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])
