.. _background:
.. index:: Background

Background
==========

Consider the function :math:`f(\theta,\phi)` defined over the surface of a unit sphere, we wish
to evaluate the integral

.. math::

    I = \int_{0}^{\pi} d\theta \; \sin \theta \int_{0}^{2\pi} d\phi \; f(\theta, \phi)

where :math:`\theta` and :math:`\phi` correspond to the polar and azimuthal angles, respectively.

Within Lebedev quadrature, this integral is approximated using a quadrature formulation as given by

.. math::

    I \approx 4 \pi \sum_{i} w_{i} f(\theta_{i},\phi_{i})

where :math:`w_{i}` are weight factors and :math:`f(\theta_{i},\phi_{i})` is the value of the function :math:`f`
evaluated at a certain point on the unit sphere.

More information on the theory behind Lebedev quadrature is provided on its `Wikipedia page <https://en.wikipedia.org/wiki/Lebedev_quadrature>`_.
