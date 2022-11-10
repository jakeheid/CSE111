from sentences import get_determiner, get_noun, get_verb, get_preposition, get_prepositional_phrase
import random
import pytest


def test_get_determiner():
    # 1. Test the single determiners.

    single_determiners = ["a", "one", "the"]

    # This loop will repeat the statements inside it 4 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a single determiner.
        word = get_determiner(1)

        # Verify that the word returned from get_determiner
        # is one of the words in the single_determiners list.
        assert word in single_determiners

    # 2. Test the plural determiners.

    plural_determiners = ["some", "many", "the"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a plural determiner.
        word = get_determiner(2)

        # Verify that the word returned from get_determiner
        # is one of the words in the plural_determiners list.
        assert word in plural_determiners

def test_get_noun():

    nouns_1 = ["adult", "bird", "boy", "car", "cat", "child", "dog",
                    "girl", "man", "rabbit", "woman"]
    nouns_2 = ["adults", "birds", "boys", "cars", "cats", "children",
                    "dogs", "girls", "men", "rabbits", "women"]
    for _ in range(4):
        assert get_noun(1) in nouns_1
        assert get_noun(2) in nouns_2

def test_get_verb():
    verbs_1 = ["drank", "ate", "grew", "laughed", "thought", "ran", "slept","talked", "walked", "wrote"]
    verbs_2 = ["will drink", "will eat", "will grow", "will laugh", "will think","will run", "will sleep", "will talk", "will walk", "will write"]
    verbs_3 = ["drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps","talks", "walks", "writes"]
    verbs_4 = ["drink", "eat", "grow", "laugh", "think", "run", "sleep","talk", "walk", "write"]
    for _ in range(4):
        assert get_verb(1,'past') in verbs_1
        assert get_verb(1,'future') in verbs_2
        assert get_verb(1,'present') in verbs_3
        assert get_verb(2,'present') in verbs_4

def test_get_preposition():
    preposition_1 = ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]
    for _ in range(4):
        assert get_preposition() in preposition_1

def test_get_prepositional_phrase():
    prep_phrase = [1, 2]
    quantity = random.choice(prep_phrase)
    get_prepositional_phrase(quantity)


# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])