import unittest
from DecodeTheMorseCode import decodeMorse


class selfDict(unittest.TestCase):
    def test_A(self):
        self.assertAlmostEquals(decodeMorse('.-'), 'A')
        self.assertAlmostEquals(decodeMorse('...---...'), 'SOS')
if __name__ == "__main__":
    unittest.main()
