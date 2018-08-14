from CalculatingWithFunctions import *
import unittest
class testClass(unittest.TestCase):
    def test_plus(self):
        self.assertAlmostEquals(four(plus(nine())), 13)
    def test_minus(self):
        self.assertAlmostEquals(eight(minus(three())), 5)
    def test_times(self):
        self.assertAlmostEquals(seven(times(five())), 35)
    def test_divided_by(self):
        self.assertAlmostEquals(six(divided_by(two())), 3)
if __name__ =="__main__":
    unittest.main()
