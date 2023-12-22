PyLebedev: Lebedev quadrature coefficients
==========================================

.. image:: https://img.shields.io/github/v/tag/ifilot/pylebedev?label=version
   :alt: GitHub tag (latest SemVer)
.. image:: https://github.com/ifilot/pylebedev/actions/workflows/build_wheels.yml/badge.svg
   :target: https://github.com/ifilot/pylebedev/actions/workflows/build_wheels.yml
.. image:: https://github.com/ifilot/pylebedev/actions/workflows/build_conda.yml/badge.svg
   :target: https://github.com/ifilot/pylebedev/actions/workflows/build_conda.yml
.. image:: https://codecov.io/gh/ifilot/pylebedev/graph/badge.svg?token=RA2HJ0QA01 
   :target: https://codecov.io/gh/ifilot/pylebedev
.. image:: https://img.shields.io/badge/License-GPLv3-blue.svg
   :target: https://www.gnu.org/licenses/gpl-3.0

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

The set of available orders and corresponding number of sampling points is given
in the table below.

.. list-table:: Integration order and number of sampling points
   :widths: 50 50
   :header-rows: 1

   * - Order
     - Number of points
   * - 3
     - 6
   * - 5
     - 14
   * - 7
     - 26
   * - 9
     - 38
   * - 11
     - 50
   * - 13
     - 74
   * - 15
     - 86
   * - 17
     - 110
   * - 19
     - 146
   * - 21
     - 170
   * - 23
     - 194
   * - 25
     - 230
   * - 27
     - 266
   * - 29
     - 302
   * - 31
     - 350
   * - 35
     - 434
   * - 41
     - 590
   * - 47
     - 770
   * - 53
     - 974
   * - 59
     - 1202
   * - 65
     - 1454
   * - 71
     - 1730
   * - 77
     - 2030
   * - 83
     - 2354
   * - 89
     - 2702
   * - 95
     - 3074
   * - 101
     - 3470
   * - 107
     - 3890
   * - 113
     - 4334
   * - 119
     - 4802
   * - 125
     - 5294
   * - 131
     - 5810

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
