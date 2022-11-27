import unittest
from unittest.main import main
import cap

class TestCap(unittest.TestCase):
    #unittest.TestCase is a base class from which TestCap will 
    # inherit.
    #A test case is the individual unit(Word 'Python' in this case) of testing.
    #It checks for a specific response to a particular set of inputs. 
    #unittest provides a base class, TestCase,
    #which may be used to create new test cases.(python Docs)
    def test_one_word(self):
        text = 'python'
        result = cap.cap_text(text) #we're importing captext from cap.py
        self.assertEqual(result,'Python')

    def test_multiple_words(self):
        text = 'monty python'
        result = cap.cap_text(text)
        self.assertEqual(result,'Monty Python')

if __name__ == '__main__':
    unittest.main()
