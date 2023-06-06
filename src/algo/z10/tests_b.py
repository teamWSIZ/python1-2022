from b import relative_list 
import unittest

class RelativeListTests(unittest.TestCase):

    def test_1(self):
        self.assertTrue(relative_list([4,5,9,-1], "<<>"))

    def test_2(self):
        self.assertTrue(relative_list([2,10,5,8,3], "<><>"))
    
if __name__ == '__main__':
    unittest.main()