from setuptools import Extension, setup
import os
import sys
import re

PKG = "pylebedev"
VERSIONFILE = os.path.join(os.path.dirname(__file__), PKG, "_version.py")
verstr = "unknown"
try:
    verstrline = open(VERSIONFILE, "rt").read()
except EnvironmentError:
    pass # Okay, there is no version file.
else:
    VSRE = r"^__version__ = ['\"]([^'\"]*)['\"]"
    mo = re.search(VSRE, verstrline, re.M)
    if mo:
        verstr = mo.group(1)
    else:
        print(r"Unable to find version in %s" % (VERSIONFILE,))
        raise RuntimeError(r"If %s.py exists, it is required to be well-formed" % (VERSIONFILE,))

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name=PKG,
    version="0.1.1.0",
    author="Ivo Filot",
    author_email="ivo@ivofilot.nl",
    description="Python package for obtaining Lebedev quadrature points and coefficients",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ifilot/pylebedev",
    packages=[PKG],
    package_data={PKG: ['data/lebedev_003.txt',
                        'data/lebedev_005.txt',
                        'data/lebedev_007.txt',
                        'data/lebedev_009.txt',
                        'data/lebedev_011.txt',
                        'data/lebedev_013.txt',
                        'data/lebedev_015.txt',
                        'data/lebedev_017.txt',
                        'data/lebedev_019.txt',
                        'data/lebedev_021.txt',
                        'data/lebedev_023.txt',
                        'data/lebedev_025.txt',
                        'data/lebedev_027.txt',
                        'data/lebedev_029.txt',
                        'data/lebedev_031.txt',
                        'data/lebedev_035.txt',
                        'data/lebedev_041.txt',
                        'data/lebedev_047.txt',
                        'data/lebedev_053.txt',
                        'data/lebedev_059.txt',
                        'data/lebedev_065.txt',
                        'data/lebedev_071.txt',
                        'data/lebedev_077.txt',
                        'data/lebedev_083.txt',
                        'data/lebedev_089.txt',
                        'data/lebedev_095.txt',
                        'data/lebedev_101.txt',
                        'data/lebedev_107.txt',
                        'data/lebedev_113.txt',
                        'data/lebedev_119.txt',
                        'data/lebedev_125.txt',
                        'data/lebedev_131.txt'
                        ]},
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX",
    ],
    python_requires='>=3.5',
    zip_safe=False,
    install_requires=['numpy'],
)
