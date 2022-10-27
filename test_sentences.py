import pytest

""""
Tests for sentences.py

"""

from sentences import get_adjective, get_determiner, get_noun, get_preposition, get_prepositional_phrase, get_verb
import random
import pytest


def test_get_determiner():

    single_determiners = ["a", "one", "the"]

    # This loop will repeat the statements inside it 4 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(4):
        word = get_determiner(1)
        assert word in single_determiners

    # 2. Test the plural determiners.

    plural_determiners = ["some", "many", "the"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):
        word = get_determiner(2)
        assert word in plural_determiners

def test_get_noun():
    
    single_nouns = ["bird", "boy", "car", "cat", "child", "dog", "girl", "man", "rabbit", "woman"]

    # This loop will repeat the statements inside it 4 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(4):
        word = get_noun(1)
        assert word in single_nouns

    # 2. Test the plural nouns.

    plural_nouns = ["birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "rabbits", "women"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):
        word = get_noun(2)
        assert word in plural_nouns

def test_get_verb():

    # Test get verb past
    verbs_past = ["drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"]

    for _ in range(4):

        word = get_verb(1, "past")
        assert word in verbs_past

    # Test get verb present single.
    verbs_present_single = ["drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"]

    for _ in range(4):

        word = get_verb(1,"present")
        assert word in verbs_present_single

    # Test get verb present plural
    verbs_present_plural = ["drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"]

    for _ in range(4):

        word = get_verb(2,"present")
        assert word in verbs_present_plural

    # Test get verb present future
    verbs_future = ["will drink", "will eat", "will grow", "will laugh", "will think", "will run", "will sleep", "will talk", "will walk", "will write"]

    for _ in range(4):

        word = get_verb(1, "future")
        assert word in verbs_future

def test_adjective():
    adjectives = ["adorable", "awful", "beautiful", "bewildered", "bored", "clumsy",
        "combative","depressed", "delightful", "foolish", "funny", "gifted", 
        "glamorous", "handsome", "grumpy", "shy", "graceful", "healthy", "hilarious", 
        "joyous", "nutty", "long", "short", "tall", "wide", "vany", "wild"]
    for _ in range(4):

        word = get_adjective()
        assert word in adjectives        
        
def test_get_preposition():
    prepostions = ["about", "above", "across", "after", "along", 
        "around", "at", "before", "behind", "below", 
        "beyond", "by", "despite", "except", "for", 
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]

    for _ in range(4):

        word = get_preposition()
        assert word in prepostions

def test_get_prepositional_phrase():
    """
    A prepositional phrase a made from 3 parts: 
    A prepostion, a determiner and a noun
    """
    prepostions = ["about", "above", "across", "after", "along", 
    "around", "at", "before", "behind", "below", 
    "beyond", "by", "despite", "except", "for", 
    "from", "in", "into", "near", "of",
    "off", "on", "onto", "out", "over",
    "past", "to", "under", "with", "without"]

    single_determiners = ["a", "one", "the"]
    plural_determiners = ["some", "many", "the"]

    single_nouns = ["bird", "boy", "car", "cat", "child", "dog", "girl", "man", "rabbit", "woman"]
    plural_nouns = ["birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "rabbits", "women"]


    # Test single version --------------
    single = 1

    # Verify that the prepositional phrase is made from 3 parts
    phrase = get_prepositional_phrase(1)

    words_in_phrase = phrase.split()
    assert len(words_in_phrase) == 3

    preposition = words_in_phrase[0]
    determiner = words_in_phrase[1]
    noun = words_in_phrase[2]

    for _ in range(4):

        assert preposition in prepostions
        assert determiner in single_determiners
        assert noun in single_nouns    

    # Test plural version --------------
    plural = 2

    # Verify that the prepositional phrase is made from 3 parts
    phrase = get_prepositional_phrase(2) 

    words_in_phrase = phrase.split()
    assert len(words_in_phrase) == 3

    preposition = words_in_phrase[0]
    determiner = words_in_phrase[1]
    noun = words_in_phrase[2]

    for _ in range(4):

        assert preposition in prepostions
        assert determiner in plural_determiners
        assert noun in plural_nouns 


# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])
