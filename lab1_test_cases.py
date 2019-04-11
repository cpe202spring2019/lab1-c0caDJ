import unittest
from lab1 import *

 # A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

    def test_max_list_iter(self):
        """testing Value errors """
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(None)

        """ Testing with normal ints and negatives, same values, floats, and inf value"""
        self.assertEqual(max_list_iter([1000,3,1,23,-123]), 1000)
        self.assertEqual( max_list_iter([1,1,1]), 1)
        self.assertEqual( max_list_iter([-1,0,1]), 1)
        self.assertEqual( max_list_iter([12.32, 123.123123123, 101010010.3939393]),  101010010.3939393)
        self.assertEqual( max_list_iter([1,2,2,3,float("inf")]), float("inf"))
        self.assertEqual( max_list_iter([]), None)

    def test_reverse_rec(self):
        """testing with Value error """
        with self.assertRaises(ValueError):  # used to check for exception
            reverse_rec(None)

        """testing with floats, ints, empty lists, same values, and single value list"""
        self.assertEqual(reverse_rec([1,2,3]),[3,2,1])
        self.assertEqual(reverse_rec([1.1,2.2,3.3]),[3.3,2.2,1.1])
        self.assertEqual(reverse_rec([1123,2123,-3]),[-3,2123,1123])
        self.assertEqual(reverse_rec([]),[])
        self.assertEqual(reverse_rec([0,0,0]),[0,0,0])
        self.assertEqual(reverse_rec([1]),[1])

    def test_bin_search(self):
        """testing with none type list """
        with self.assertRaises(ValueError):  # used to check for exception
            bin_search(0, 1,2, None)
            
        """testing with ints, negatives, single value lists, even, odd length list and lists with none value"""
        list_val =[0,1,2,3,4,7,9,10 ]# even length case
        low = 0

        i = [-1,1,3,4,5] # odd length case
        j = [9]
        m = [0, 1, 2, None]
        self.assertEqual(bin_search(0, low, len(list_val)-1, list_val), 0 )
        self.assertEqual(bin_search(-1, low, len(i)-1, i) , 0)
        self.assertEqual(bin_search(9, low, len(j)-1, j) , 0)
        self.assertEqual(bin_search(2, low, len(m)-1, m) , 2)
        self.assertEqual(bin_search(1000, low, len(i)-1, i) , None)


if __name__ == "__main__":
    unittest.main()

    
