
import unittest
import re

def are_keywords_in_title(title, keywords):
    '''check some keywords to see if the title is related'''
    # please write your code here

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
        result = is_star_trek('Actor Chris Pine Is Amazing')
        self.assertTrue(result)

if __name__ == "__main__":
    unittest.main()


