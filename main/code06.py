
import unittest
import re
import code02
import code05

def get_scores():
    path = '../data/clickbait-input-data'
    total_score_star_wars = 0.0
    total_score_star_trek = 0.0
    # please write code here to loop through the file and 
    # split by ; to get the items.
    # items[1] is the date
    # items[2] is the number of likes
    # items[3] is the title
    # use code02.get_score to get how much the score should be increased
    # use code05.is_star_wars_improved to return the number of lines that are starwars related
    return total_score_star_wars, total_score_star_trek

# you can write some tests here and run this script
# to see if your code is working as expected
class Tests(unittest.TestCase):
    def test_get_scores(self):
        total_score_star_wars, total_score_star_trek = get_scores()
        print('test not yet written')

if __name__ == "__main__":
    unittest.main()


