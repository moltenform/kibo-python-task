
import unittest
import code01

def count_data_lines():
    path = '../data/clickbait-input-data'
    number_of_lines = 0
    with open(path) as f:
        for line in f:
            if not line:
                continue
            number_of_lines += 1
    return number_of_lines

def count_star_wars_related():
    path = '../data/clickbait-input-data'
    number_of_lines = 0
    with open(path) as f:
        for line in f:
            if not line:
                continue
            items = line.split(';')
            title = items[3]
            if code01.is_star_wars(title):
                number_of_lines += 1
    return number_of_lines

# you can write some tests here and run this script
# to see if your code is working as expected
class Tests(unittest.TestCase):
    def test_count_data_lines(self):
        result = count_data_lines()
        self.assertEqual(15999, result)
    def test_count_star_wars_related(self):
        result = count_star_wars_related()
        self.assertEqual(150, result)

if __name__ == "__main__":
    unittest.main()

