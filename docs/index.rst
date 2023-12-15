PyLebedev: Lebedev quadrature coefficients
==========================================

:program:`PyLebedev` is a pure-Python package for handling integration of function
over the surface of a unit sphere by means of `Lebedev quadrature <https://en.wikipedia.org/wiki/Lebedev_quadrature>`_.

A simple example how PyLebedev works is given below

.. code:: python

   from pylebedev import PyLebedev
   import numpy as np

   def main():
      """
      Test Lebedev quadrature for probe function
      """
      # build library
      leblib = PyLebedev()
      
      # exact answer to function "testfunc"
      exact = 216.0 * np.pi / 35.0
      r,w = leblib.get_points_and_weights(9)
      integral = 4.0 * np.pi * np.sum(w * tfunc(r[:,0], r[:,1], r[:,2]))
      
      print('Integral: %f vs Exact: %f' % (integral, exact))

   def tfunc(x,y,z):
      """
      Trial function to test
      
      Adapted from: https://cbeentjes.github.io/files/Ramblings/QuadratureSphere.pdf
      
      This function has the exact result upon integration over a unit sphere
      of 216/35 * pi
      """
      return 1 + x + y**2 + x**2*y + x**4 + y**5 + x**2*y**2*z**2

   if __name__ == '__main__':
      main()

The result of this code is::

   Integral: 19.388115 vs Exact: 19.388115

:program:`PyLebedev` has been developed at the Eindhoven University of Technology,
Netherlands. :program:`PyLebedev` and its development are hosted on `github
<https://gitlab.tue.nl/ifilot/pydft>`_.  Bugs and feature
requests are ideally submitted via the `github issue tracker
<https://gitlab.tue.nl/ifilot/pydft/issues>`_.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   installation
   background
   usage
   community_guidelines

Indices and tables
------------------

* :ref:`genindex`
* :ref:`search`
