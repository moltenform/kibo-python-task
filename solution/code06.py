
import unittest
import re
import code02
import code05

def get_scores():
    path = '../data/clickbait-input-data'
    total_score_star_wars = 0.0
    total_score_star_trek = 0.0
    with open(path) as f:
        for line in f:
            if not line:
                continue
            items = line.split(';')
            date = items[1]
            s_likes = items[2]
            title = items[3]
            score = code02.get_score(date, s_likes, title)
            if code05.is_star_wars_improved(title):
                total_score_star_wars += score
            if code05.is_star_trek_improved(title):
                total_score_star_trek += score
    print('total_score_star_wars', total_score_star_wars)
    print('total_score_star_trek', total_score_star_trek)
    return total_score_star_wars, total_score_star_trek

# you can write some tests here and run this script
# to see if your code is working as expected
class Tests(unittest.TestCase):
    def test_get_scores(self):
        total_score_star_wars, total_score_star_trek = get_scores()
        

if __name__ == "__main__":
    unittest.main()


