.. -*- coding: utf-8 -*-
.. _runners:

:mod:`gada_pyrunner` - Runners
==============================

Here is a full list of runners included in this package.

pymodule Runner
===============

.. automodule:: gada_pyrunner.pymodule

Full configuration
------------------

Based on Python package structure shown above:

.. code-block:: yaml

    nodes:
      mynode:
        runner: pymodule
        [module: gadalang_mycomponent.mynode]
        [entrypoint: main]

Parameters:

- ``module``: Optional - Python module to load (default is ``gadalang_mycomponent``)
- ``entrypoint``: Optional - Function to call from ``module`` (default is ``main``)

Handle command line arguments
-----------------------------

The :mod:`pymodule` runner will call the entrypoint configured in ``config.yml`` with the
command line arguments. You can retrieve them by adding an ``argv`` parameter to
your entrypoint.

Content of ``mynode.py``:

.. code-block:: python

    def main(argv, **kwargs):
        print(argv)

Usage:

.. code-block:: bash

    $ gada mycomponent.mynode 1 2
    ['mycomponent.mynode', '1', '2']

.. note:: ``argv[0]`` is the module that is loaded.
