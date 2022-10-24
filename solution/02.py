
import unittest
from datetime import datetime

def get_score(title, s_likes, s_article_date):
    '''get the popularity score for an article taking into account # of likes'''
    return 1 + float(s_likes) / 100.0

def get_score_extra_credit(title, s_likes, s_article_date):
    '''get the popularity score for an article taking into account # of likes'''
    score = 1 + float(s_likes) / 100.0
    dt = datetime.fromisoformat(s_article_date)
    days_in_year = 365
    if (datetime.now() - dt).days < 5 * days_in_year:
        score *= 1.25
        
    return score
    

# you can write some tests here and run this script
# to see if your code is working as expected
class TestLogAnalyzer(unittest.TestCase):
    def test_get_score_with_5_likes(self):
        result = get_score('Test', 5, '2015-12-20')
        self.assertAlmostEqual(result, 1.05)
    def test_get_score_extra_credit_not_new_enough(self):
        result = get_score_extra_credit('Test', 5, '2015-12-20')
        self.assertAlmostEqual(result, 1.05)
    def test_get_score_extra_credit_new_enough(self):
        result = get_score_extra_credit('Test', 5, '2020-12-20')
        self.assertAlmostEqual(result, 1.3125)

if __name__ == "__main__":
    unittest.main()

