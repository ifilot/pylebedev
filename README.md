# PyLebedev

[![C/C++ CI](https://github.com/ifilot/pylebedev/actions/workflows/build.yml/badge.svg)](https://github.com/ifilot/pylebedev/actions/workflows/build.yml)
[![Anaconda-Server Badge](https://anaconda.org/ifilot/pylebedev/badges/version.svg)](https://anaconda.org/ifilot/pylebedev)
[![PyPI](https://img.shields.io/pypi/v/pylebedev?color=green)](https://pypi.org/project/pylebedev/)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)


## Purpose

PyLebedev is a python package that stores Lebedev quadrature coefficients for integration over the unit sphere.

## Installation

### Anaconda

[![Anaconda Version](https://anaconda.org/ifilot/pylebedev/badges/version.svg)](https://anaconda.org/ifilot/pylebedev)
[![Anaconda Platforms](https://anaconda.org/ifilot/pylebedev/badges/platforms.svg)](https://anaconda.org/ifilot/pylebedev)
[![Anaconda Downloads](https://anaconda.org/ifilot/pylebedev/badges/downloads.svg)](https://anaconda.org/ifilot/pylebedev)

Open Anaconda prompt and type

```
conda install -c ifilot pylebedev
```

### PyPi

[![PyPI](https://img.shields.io/pypi/v/pylebedev?color=green)](https://pypi.org/project/pylebedev/)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/pypi)](https://pypi.org/project/pylebedev/)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pylebedev)


Open a terminal and type

```
pip install pylebedev
```

## Usage

```python
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
```