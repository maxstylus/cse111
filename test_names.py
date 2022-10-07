from names import make_full_name, \
    extract_family_name, extract_given_name
import pytest

def test_make_full_name():
    assert make_full_name("Sally", "Mayfield") == "Mayfield; Sally"
    assert make_full_name("SALLY", "MAYFIELD") == "Mayfield; Sally"
    assert make_full_name("Jean-Paul", "Satre") == "Satre; Jean-Paul"
    assert make_full_name("Leilani", "Ka'anapali") == "Ka'anapali; Leilani"
    assert make_full_name("Mark", "Smith-Allen") == "Smith-Allen; Mark"

def test_extract_family_name():
    assert extract_family_name("Mayfield; Sally") == "Mayfield"
    assert extract_family_name("MAYFIELD; SALLY") == "Mayfield"
    assert extract_family_name("Satre; Jean-Paul") == "Satre"
    assert extract_family_name("Ka'anapali; Leilani") == "Ka'anapali"
    assert extract_family_name("Smith-Allen; Mark") == "Smith-Allen"

def test_extract_given_name():
    assert extract_given_name("Mayfield; Sally") == "Sally"
    assert extract_given_name("MAYFIELD; SALLY") == "Sally"
    assert extract_given_name("Satre; Jean-Paul") == "Jean-Paul"
    assert extract_given_name("Ka'anapali; Leilani") == "Leilani"
    assert extract_given_name("Smith-Allen; Mark") == "Mark"


# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])