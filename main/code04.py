
import unittest

def is_star_wars_improved(title):
    '''check some keywords to see if the title is related to star wars'''
    # please write your code here

# you can write some tests here and run this script
# to see if your code is working as expected
class Tests(unittest.TestCase):
    def test_recognizes_star_wars_actor(self):
        result = is_star_wars_improved('Actor Mark Hamill Is Amazing')
        self.assertTrue(result)
    def test_does_not_recognize_other_actor(self):
        result = is_star_wars_improved('Quotes From Frank Reynolds')
        self.assertFalse(result)

if __name__ == "__main__":
    unittest.main()


