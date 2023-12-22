.. _installation:
.. index:: Installation

Installation
============

:program:`PyLebedev` can be obtained either via Anaconda or via PyPi.

Anaconda
--------

.. image:: https://anaconda.org/ifilot/pylebedev/badges/version.svg
   :target: https://anaconda.org/ifilot/pylebedev
.. image:: https://anaconda.org/ifilot/pylebedev/badges/platforms.svg
   :target: https://anaconda.org/ifilot/pylebedev
.. image:: https://anaconda.org/ifilot/pylebedev/badges/downloads.svg
   :target: https://anaconda.org/ifilot/pylebedev

.. code ::

    conda install -c ifilot pylebedev

PyPi
----

.. image:: https://img.shields.io/pypi/v/pylebedev?color=green
   :target: https://pypi.org/project/pylebedev/
.. image:: https://img.shields.io/pypi/dm/pypi
   :target: https://pypi.org/project/pylebedev/
.. image:: https://img.shields.io/pypi/pyversions/pylebedev
   :target: https://pypi.org/project/pylebedev/

.. code ::

    pip install pylebedev

Testing
-------

.. image:: https://codecov.io/gh/ifilot/pylebedev/graph/badge.svg?token=RA2HJ0QA01 
 :target: https://codecov.io/gh/ifilot/pylebedev

To test PyLebedev, one can run the following from the root folder of the repository

```bash
python -m pytest tests/*.py
```