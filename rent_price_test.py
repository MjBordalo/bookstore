import unittest
from rent_price import *
from datetime import  datetime,timedelta,date

d1 = date(2020, 5, 17)
d_after = date(2020, 5, 25)

class TestRentPrice(unittest.TestCase):
    def test_compute_price1(self):

        #valid test
        self.assertAlmostEqual(compute_price1(d1,d_after),8)
        self.assertAlmostEqual(compute_price1(d1,d1),0)

    def test_asserts(self):
        self.assertRaises(ValueError, compute_price1,d_after, d1)
        self.assertRaises(TypeError, compute_price1, "d_after", d1)

