
import unittest
import re

def are_keywords_in_title(title, keywords):
    '''check some keywords to see if the title is related'''
    for keyword in keywords:
        regexp = rf'\b{keyword}\b'
        if re.search(regexp, title):
            return True
    return False

def is_star_wars_improved(title):
    star_wars_keywords = 'Star Wars,The Force,John Boyega,Carrie Fisher,Mark Hamill,Rey'.split(',')
    return are_keywords_in_title(title, star_wars_keywords)
    
def is_star_trek_improved(title):
    star_trek_keywords = 'Star Trek,Warp Drive,Chris Pine,Kate Mulgrew,George Takei'.split(',')
    return are_keywords_in_title(title, star_trek_keywords)

# you can write some tests here and run this script
# to see if your code is working as expected
class Tests(unittest.TestCase):
    def test_recognizes_star_trek_actor(self):
        result = is_star_trek_improved('Actor Chris Pine Is Amazing')
        self.assertTrue(result)
    def test_recognizes_star_wars_actor(self):
        result = is_star_wars_improved('Actor Mark Hamill Is Amazing')
        self.assertTrue(result)
    def test_for_star_trek_should_not_accept_star_wars(self):
        result = is_star_trek_improved('Article About Star Wars')
        self.assertFalse(result)
    def test_for_star_wars_should_not_accept_star_trek(self):
        result = is_star_wars_improved('Article About Star Trek')
        self.assertFalse(result)
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

