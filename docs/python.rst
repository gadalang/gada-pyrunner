.. -*- coding: utf-8 -*-
.. _python:

python
======

.. automodule:: gada_pyrunner.python

Full configuration
------------------

.. code-block:: yaml

    nodes:
      mynode:
        runner: python
        [bin: python]
        file: mynode.py

Parameters:

- ``bin``: Optional - Python bin to use in command line (default is ``python``)
- ``file``: Python script to run (relative to ``gadalang_mycomponent``)
