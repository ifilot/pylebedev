import unittest
import numpy as np

import os,sys

# add a reference to load the module
ROOT = os.path.dirname(__file__)
sys.path.insert(0, os.path.join(ROOT, '..'))

from pylebedev import PyLebedev

class TestLebedevClass(unittest.TestCase):

    def test_order_list(self):
        leblib = PyLebedev()
        np.testing.assert_equal(leblib.get_orders_list(),
                                [3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 35, 41, 47, 53, 59, 65, 71, 77, 83, 89, 95, 101, 107, 113, 119, 125, 131])
        
    def test_nrpoints_list(self):
        leblib = PyLebedev()
        np.testing.assert_equal(leblib.get_nrpoints_list(),
        [6, 14, 26, 38, 50, 74, 86, 110, 146, 170, 194, 230, 266, 302, 350, 434, 590, 770, 974, 1202, 1454, 1730, 2030, 2354, 2702, 3074, 3470, 3890, 4334, 4802, 5294, 5810])

if __name__ == '__main__':
    unittest.main()
