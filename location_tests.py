import unittest
from location import *

class TestLab1(unittest.TestCase):

    def test_repr(self):
        loc = Location("SLO", 35.3, -120.7)
        self.assertEqual(repr(loc),"Location('SLO', 35.3, -120.7)")
    
    def test_eq(self):
        loc = Location("SLO", 35.3, -120.7)
        loc2 = Location("JON", 3.3, -12.7)

        self.assertFalse(loc == loc2)
    # Add more tests!

if __name__ == "__main__":
        unittest.main()
