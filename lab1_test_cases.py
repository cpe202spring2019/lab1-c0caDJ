import unittest
from lab1 import *

 # A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

    def test_max_list_iter(self):
        """testing type errors with strings, None type , and empty list"""
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(None)
            max_list_iter(["asd", " d" , " asd"])

        """ Testing with normal ints and negatives, same values, floats, and inf value"""
        self.assertEqual(max_list_iter([1000,3,1,23,-123]), 1000)
        self.assertEqual( max_list_iter([1,1,1]), 1)
        self.assertEqual( max_list_iter([-1,0,1]), 1)
        self.assertEqual( max_list_iter([12.32, 123.123123123, 101010010.3939393]),  101010010.3939393)
        self.assertEqual( max_list_iter([1,2,2,3,float("inf")]), float("inf"))
        self.assertEqual( max_list_iter([]), None)

    def test_reverse_rec(self):
        """testing with type error none and strings"""
        with self.assertRaises(ValueError):  # used to check for exception
            reverse_rec(None)
            reverse_rec(["asd", "asdf", "asdfasd"])

        """testing with floats, ints, empty lists, same values, and single value list"""
        self.assertEqual(reverse_rec([1,2,3]),[3,2,1])
        self.assertEqual(reverse_rec([1.1,2.2,3.3]),[3.3,2.2,1.1])
        self.assertEqual(reverse_rec([1123,2123,-3]),[-3,2123,1123])
        self.assertEqual(reverse_rec([]),[])
        self.assertEqual(reverse_rec([0,0,0]),[0,0,0])
        self.assertEqual(reverse_rec([1]),[1])

    def test_bin_search(self):
        """testing with none type list and list with none type"""
        with self.assertRaises(ValueError):  # used to check for exception
            bin_search(0, 1,2, None)
            n = [1,2,3,None]
            bin_search(1, 0, len(n), n)
            
        """testing with ints, negatives, single value lists, and lists with none value"""
        list_val =[0,1,2,3,4,7,9,10 ]
        low = 0

        i = [-1,1,3,4,5] 
        j = [9]
        m = [0, 1, 2, None]
        self.assertEqual(bin_search(0, low, len(list_val), list_val), 0 )
        self.assertEqual(bin_search(-1, low, len(i), i) , 0)
        self.assertEqual(bin_search(9, low, len(j), j) , 0)
        self.assertEqual(bin_search(2, low, len(m), m) , 2)


if __name__ == "__main__":
    unittest.main()

    
