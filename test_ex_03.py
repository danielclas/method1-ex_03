import unittest
from ex_03 import *


class TestAssignment(unittest.TestCase):

    def test_tokenize_space(self):
        sentence_one = "This is a sentence, albeit a simple one."
        expected_one = ['This', 'is', 'a', 'sentence,', 'albeit', 'a', 'simple', 'one.']
        sentence_two = "Just a sentence."
        expected_two = ['Just', 'a', 'sentence.']
        self.assertEqual(expected_one, tokenize_space(sentence_one))
        self.assertEqual(expected_two, tokenize_space(sentence_two))

    def test_tokenize_smart(self):
        sentence_one = "This is a sentence, albeit a simple one."
        expected_one = ['This', 'is', 'a', 'sentence', ',', 'albeit', 'a', 'simple', 'one', '.']
        sentence_two = "Just a sentence."
        expected_two = ['Just', 'a', 'sentence', '.']
        self.assertEqual(expected_one, tokenize_smart(sentence_one))
        self.assertEqual(expected_two, tokenize_smart(sentence_two))

    def test_is_auxiliary(self):
        self.assertEqual(True, is_auxiliary("been"))
        self.assertEqual(False, is_auxiliary("rise"))

    def test_is_determiner(self):
        self.assertEqual(True, is_determiner("another"))
        self.assertEqual(False, is_determiner("their"))

    def test_is_preposition(self):
        self.assertEqual(True, is_preposition("on"))
        self.assertEqual(False, is_preposition("one"))

    def test_is_nominative_pronoun(self):
        self.assertEqual(True, is_subject_pronoun("i"))
        self.assertEqual(False, is_subject_pronoun("my"))

    def test_normalize(self):
        self.assertEqual("has", normalize("Hasn't"))
        self.assertEqual("is", normalize("Isn't"))

    def test_detect_pos_tag(self):
        self.assertEqual("VERB", detect_pos("They force me to speak!"))
        self.assertEqual("NOUN", detect_pos("May the force be with you."))
        self.assertEqual("Unknown", detect_pos("I run force."))

if __name__ == '__main__':
    unittest.main()
