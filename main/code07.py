
import unittest
import re
import code02
import code05

class BaseKeywordChecker():
    def __init__(self, name, keywords):
        self.keywords = keywords
        
    def check(self, title):
        return code05.are_keywords_in_title(title, self.keywords)

class StarWarsChecker(BaseKeywordChecker):
    def __init__(self):
        # fill this out
    
class StarTrekChecker(BaseKeywordChecker):
    def __init__(self):
        # fill this out

def get_scores(listOfCheckers):
    # listOfCheckers is a list of BaseKeywordChecker objects
    path = '../data/clickbait-input-data'
    scores = {}
    for checker in listOfCheckers:
        scores[checker.name] = 0.0
        
    # please write code here to loop through the file and 
    # split by ; to get the items.
    # items[1] is the date
    # items[2] is the number of likes
    # items[3] is the title
    
    # this snippet will be helpful:
    # for checker in listOfCheckers:
    #   if checker.check(title):
    #     scores[checker.name] += score
    
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


