
import unittest
import re
import code02
import code04
import code05


class BaseKeywordChecker():
    def __init__(self, name, keywords):
        self.name = name
        self.keywords = keywords
        
    def check(self, title):
        return code05.are_keywords_in_title(title, self.keywords)

class StarWarsChecker(BaseKeywordChecker):
    def __init__(self):
        # not using super() as we are at a beginner level
        self.name = 'star wars'
        self.keywords = code04.star_wars_keywords
    
class StarTrekChecker(BaseKeywordChecker):
    def __init__(self):
        # not using super() as we are at a beginner level
        self.name = 'star trek'
        self.keywords = code04.star_trek_keywords

def get_scores(listOfCheckers):
    # listOfCheckers is a list of BaseKeywordChecker objects
    path = '../data/clickbait-input-data'
    scores = {}
    for checker in listOfCheckers:
        scores[checker.name] = 0.0
    
    with open(path) as f:
        for line in f:
            if not line:
                continue
            items = line.split(';')
            date = items[1]
            s_likes = items[2]
            title = items[3]
            score = code02.get_score(date, s_likes, title)
            for checker in listOfCheckers:
              if checker.check(title):
                scores[checker.name] += score
    
    print("Here are the results!")
    print(scores)
    return scores

# you can write some tests here and run this script
# to see if your code is working as expected
class Tests(unittest.TestCase):
    def test_get_scores(self):
        listOfCheckers = [StarWarsChecker(), StarTrekChecker()]
        scores = get_scores(listOfCheckers)
        print('test not yet written')

if __name__ == "__main__":
    unittest.main()


