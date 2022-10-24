

import unittest

star_wars_keywords = 'Star Wars,The Force,John Boyega,Carrie Fisher,Mark Hamill'.split(',')
def is_star_wars(title):
    '''check some keywords to see if the title is related to star wars'''
    for keyword in star_wars_keywords:
        if keyword in title:
            return True
    return False


star_trek_keywords = 'Star Trek,Warp Drive,Chris Pine,Kate Mulgrew,George Takei'.split(',')
def is_star_trek(title):
    '''check some keywords to see if the title is related to star trek'''
    for keyword in star_trek_keywords:
        if keyword in title:
            return True
    return False

# you can write some tests here and run this script
# to see if your code is working as expected
class TestLogAnalyzer(unittest.TestCase):
    def test_recognizes_star_trek_actor(self):
        result = is_star_trek('Actor Chris Pine Is Amazing')
        self.assertTrue(result)
    def test_recognizes_star_wars_actor(self):
        result = is_star_wars('Actor Mark Hamill Is Amazing')
        self.assertTrue(result)
    def test_for_star_trek_should_not_accept_star_wars(self):
        result = is_star_trek('Article About Star Wars')
        self.assertFalse(result)
    def test_for_star_wars_should_not_accept_star_trek(self):
        result = is_star_wars('Article About Star Trek')
        self.assertFalse(result)

if __name__ == "__main__":
    unittest.main()

