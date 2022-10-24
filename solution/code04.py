
import unittest
import re

star_wars_keywords = 'Star Wars,The Force,John Boyega,Carrie Fisher,Mark Hamill,Rey'.split(',')
star_trek_keywords = 'Star Trek,Warp Drive,Chris Pine,Kate Mulgrew,George Takei'.split(',')
def is_star_wars_improved(title):
    '''check some keywords to see if the title is related to star wars'''
    for keyword in star_wars_keywords:
        regexp = rf'\b{keyword}\b'
        if re.search(regexp, title):
            return True
    return False

# you can write some tests here and run this script
# to see if your code is working as expected
class Tests(unittest.TestCase):
    def test_recognizes_star_wars_actor(self):
        result = is_star_wars_improved('Actor Mark Hamill Is Amazing')
        self.assertTrue(result)
    def test_does_not_recognize_other_actor(self):
        result = is_star_wars_improved('Quotes From Frank Reynolds')
        self.assertFalse(result)
    def test_mid_string(self):
        result = is_star_wars_improved('Is Rey The')
        self.assertTrue(result)
    def test_start_string(self):
        result = is_star_wars_improved('Rey Is')
        self.assertTrue(result)
    def test_end_string(self):
        result = is_star_wars_improved('Is Rey')
        self.assertTrue(result)
    def test_dbl_quotes_string(self):
        result = is_star_wars_improved('Is "Rey"')
        self.assertTrue(result)
    def test_single_quotes_string(self):
        result = is_star_wars_improved('Is \'Rey\'')
        self.assertTrue(result)
    

if __name__ == "__main__":
    unittest.main()

