import unittest
from WhoLikesIt import likes

class selfDict(unittest.TestCase):
    def test_Null(self):
        self.assertAlmostEquals(likes([]), 'no one likes this')

    def test_One(self):
        self.assertAlmostEquals(likes(['Peter']), 'Peter likes this')

    def test_Tow(self):
        self.assertAlmostEquals(
            likes(['Jacob', 'Alex']), 'Jacob and Alex like this')

    def test_Three(self):
        self.assertAlmostEquals(
            likes(['Max', 'John', 'Mark']), 'Max, John and Mark like this')

    def test_More(self):
        self.assertAlmostEquals(
            likes(['Alex', 'Jacob', 'Mark', 'Max']), 'Alex, Jacob and 2 others like this')
if __name__ == "__main__":
    unittest.main()
