
import unittest
import code01

def count_data_lines():
    path = '../data/clickbait-input-data'
    number_of_lines = 0
    # please write code here to loop through the file and return the number of lines

def count_star_wars_related():
    path = '../data/clickbait-input-data'
    number_of_lines = 0
    # please write code here to loop through the file and 
    # split by ; to get the items.
    # use code01.is_star_wars to return the number of lines that are starwars related
    

# you can write some tests here and run this script
# to see if your code is working as expected
class Tests(unittest.TestCase):
    def test_count_data_lines(self):
        result = count_data_lines()
        self.assertEqual(15999, result)
    def test_count_star_wars_related(self):
        result = count_star_wars_related()
        self.assertEqual(888, result)


if __name__ == "__main__":
    unittest.main()

