
import unittest

def is_star_wars(title):
    '''check some keywords to see if the title is related to star wars'''
    # please write your code here


def is_star_trek(title):
    '''check some keywords to see if the title is related to star trek'''
    # please write your code here

# you can write some tests here and run this script
# to see if your code is working as expected
class TestLogAnalyzer(unittest.TestCase):
    def test_recognizes_star_trek_actor(self):
        result = is_star_trek('Actor Chris Pine Is Amazing')
        self.assertTrue(result)

if __name__ == "__main__":
    unittest.main()

