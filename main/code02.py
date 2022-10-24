
import unittest

def get_score(title, s_likes, s_article_date):
    '''get the popularity score for an article taking into account # of likes'''
    # please write your code here
    # you can ignore the title and s_article_date for now.

# you can write some tests here and run this script
# to see if your code is working as expected
class Tests(unittest.TestCase):
    def test_get_score_with_5_likes(self):
        result = get_score('Test', 5, '2015-12-20')
        self.assertAlmostEqual(result, 1.05)

if __name__ == "__main__":
    unittest.main()

