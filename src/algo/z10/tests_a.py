from a import longest_streak 
import unittest

class LongestStreakTests(unittest.TestCase):

    def test_1(self):
        self.assertEquals(longest_streak("<<>"), 2)

    def test_2(self):
        self.assertEquals(longest_streak("<>"), 1)

    def test_3(self):
        self.assertEquals(longest_streak("<>>><<"), 3)

if __name__ == '__main__':
    unittest.main()