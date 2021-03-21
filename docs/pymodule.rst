.. -*- coding: utf-8 -*-
.. _runners:

:mod:`gada_pyrunner` - Runners
==============================

Here is a full list of runners included in this package.

pymodule
========

.. automodule:: gada_pyrunner.pymodule

Full configuration
------------------

.. code-block:: yaml

    nodes:
      mynode:
        runner: pymodule
        [module: gadalang_mycomponent.mynode]
        [entrypoint: main]

Parameters:

- ``module``: Optional - Python module to load (default is ``gadalang_mycomponent``)
- ``entrypoint``: Optional - Function to call from ``module`` (default is ``main``)
