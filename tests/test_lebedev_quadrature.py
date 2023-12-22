import unittest
import numpy as np
from pylebedev import PyLebedev

class TestLebedevQuadrature(unittest.TestCase):
    """
    Test routine to check that points and weights are correctly extracted
    and can be used in Lebedev quadrature
    """

    def test_quadrature(self):
        """
        Test Lebedev quadrature for probe function
        """
        # build library
        leblib = PyLebedev()
        
        # exact answer to function "testfunc"
        exact = 216.0 * np.pi / 35.0

        for order in [7,9,11,13,15]:
            r,w = leblib.get_points_and_weights(order)
            
            integral = 4.0 * np.pi * np.sum(w * tfunc(r[:,0], r[:,1], r[:,2]))
            
            np.testing.assert_almost_equal(integral, exact, 4)
            
    def test_num_points(self):
        """
        Test assessment of number of points
        """
        # build library
        leblib = PyLebedev()
        
        np.testing.assert_equal(leblib.get_num_points(7), 26)
        np.testing.assert_equal(leblib.get_num_points(19), 146)

    def test_weights_unity(self):
        """
        Check that the sum of all the weights adds up to unity
        """
        # build library
        leblib = PyLebedev()

        for o in leblib.get_orders_list():
            sumweights = np.sum(leblib.get_points_and_weights(o, solid_angles=True)[1])
            np.testing.assert_almost_equal(sumweights, 1.0)

    def test_exceptions(self):
        # build library
        leblib = PyLebedev()
        
        # try to get points for an order that does not exist
        self.assertRaises(Exception, leblib.get_points_and_weights, 1)
        
        # try to get number of points for an order that does not exist
        self.assertRaises(Exception, leblib.get_num_points, 1)

def tfunc(x,y,z):
    """
    Trial function to test
    
    Adapted from: https://cbeentjes.github.io/files/Ramblings/QuadratureSphere.pdf
    
    This function has the exact result upon integration over a unit sphere
    of 216/35 * pi
    """
    return 1 + x + y**2 + x**2*y + x**4 + y**5 + x**2*y**2*z**2

if __name__ == '__main__':
    unittest.main()
