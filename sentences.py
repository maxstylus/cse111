from distutils.command.build import build
import random

def main():
    """
    Generate and print six sentences. 
    Each sentence must have: a determiner, a noun, a verb, a prepostional phrase. 
    The six sentences must have the following characteristics: 
    
    Quantity | Verb Tense
    single   | past
    single   | present
    single   | future
    plural   | past
    plural   | present 
    plural   | future

    """
    print()

    # Single::Past
    build_and_print_sentence("past")
    # Single::Present
    build_and_print_sentence("present")
    # Single::Future
    build_and_print_sentence("future")
    # Plural::Past
    build_and_print_sentence("past", 2)
    # Plural::Present
    build_and_print_sentence("present", 2)
    # Plural::Future
    build_and_print_sentence("future", 2)

    print()
        

def build_and_print_sentence(tense, quantity=1):
    """
    Generates and prints a sentence given the tense and whether or not it should be single or plural.
    Single is default.
    Sentences are generating by combing: 
    a determiner, a noun, a verb and a prepositional phrase.
    """
    determiner = get_determiner(quantity).capitalize()
    adjective = get_adjective()
    noun = get_noun(quantity)
    verb = get_verb(quantity, tense)
    prepositional_phrase = get_prepositional_phrase(quantity)
    
    print(f"{determiner} {adjective} {noun} {verb} {prepositional_phrase}.")

def get_determiner(quantity):
    """Return a randomly chosen determiner. A determiner is
    a word like "the", "a", "one", "some", "many".
    If quantity == 1, this function will return either "a",
    "one", or "the". Otherwise this function will return
    either "some", "many", or "the".

    Parameter
        quantity: an integer.
            If quantity == 1, this function will return a
            determiner for a single noun. Otherwise this
            function will return a determiner for a plural
            noun.
    Return: a randomly chosen determiner.
    """
    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["some", "many", "the"]

    # Randomly choose and return a determiner.
    word = random.choice(words)
    return word

def get_noun(quantity):
    """Return a randomly chosen noun.
    If quantity == 1, this function will
    return one of these ten single nouns:
        "bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"
    Otherwise, this function will return one of
    these ten plural nouns:
        "birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"

    Parameter
        quantity: an integer that determines if
            the returned noun is single or plural.
    Return: a randomly chosen noun.
    """
    if quantity == 1:
        words = ["bird", "boy", "car", "cat", "child", "dog", "girl", "man", "rabbit", "woman"]
    else:
        words = ["birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "rabbits", "women"]

    # Randomly choose and return a determiner.
    word = random.choice(words)
    return word

def get_verb(quantity, tense):
    """Return a randomly chosen verb. If tense is "past",
    this function will return one of these ten verbs:
        "drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"
    If tense is "present" and quantity is 1, this
    function will return one of these ten verbs:
        "drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"
    If tense is "present" and quantity is NOT 1,
    this function will return one of these ten verbs:
        "drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"
    If tense is "future", this function will return one of
    these ten verbs:
        "will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"

    Parameters
        quantity: an integer that determines if the
            returned verb is single or plural.
        tense: a string that determines the verb conjugation,
            either "past", "present" or "future".
    Return: a randomly chosen verb.
    """


    if tense == "past": 

        words = ["drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"]

    elif tense == "present": 
        if quantity == 1: 
            # quantity = 1 and tense = present
            words = ["drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"]
        else: 
            # quantity is != 1 and tense = present 
            words = ["drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"]
    elif tense == "future": 
        words = ["will drink", "will eat", "will grow", "will laugh", "will think", "will run", "will sleep", "will talk", "will walk", "will write"]
    
    # Randomly choose and return a determiner.
    word = random.choice(words)
    return word

def get_adjective():
    """Return a randomly chosen preposition
    from this list of prepositions:

    Return: a randomly chosen adjective.
    """
    adjectives = ["adorable", "awful", "beautiful", "bewildered", "bored", "clumsy",
            "combative","depressed", "delightful", "foolish", "funny", "gifted", 
            "glamorous", "handsome", "grumpy", "shy", "graceful", "healthy", "hilarious", 
            "joyous", "nutty", "long", "short", "tall", "wide", "vany", "wild"]

    # Randomly choose and return a determiner.
    word = random.choice(adjectives)
    return word

def get_preposition():
    """Return a randomly chosen preposition
    from this list of prepositions:
        "about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"

    Return: a randomly chosen preposition.
    """
    words = ["about", "above", "across", "after", "along", 
        "around", "at", "before", "behind", "below", 
        "beyond", "by", "despite", "except", "for", 
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]

    # Randomly choose and return a determiner.
    word = random.choice(words)
    return word

def get_prepositional_phrase(quantity):
    """Build and return a prepositional phrase composed of three
    words: a preposition, a determiner, and a noun by calling the
    get_preposition, get_determiner, and get_noun functions.

    Parameter
        quantity: an integer that determines if the determiner
            and noun in the prepositional phrase returned from
            this function are single or pluaral.
    Return: a prepositional phrase.
    """

    preposition = get_preposition()
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)

    prepostional_phrase = preposition + " " + determiner + " " + noun

    return prepostional_phrase

if __name__ == "__main__":
    main()