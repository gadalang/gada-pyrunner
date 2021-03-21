.. -*- coding: utf-8 -*-
.. _python:

python
======

.. automodule:: gada_pyrunner.python

Full configuration
------------------

Based on Python package structure shown above:

.. code-block:: yaml

    nodes:
      mynode:
        runner: python
        [bin: python]
        file: mynode.py

Parameters:

- ``bin``: Optional - Python bin to use in command line (default is ``python``)
- ``file``: Python script to run (relative to ``gadalang_mycomponent``)

Handle command line arguments
-----------------------------

The :mod:`python` runner will run your gada node as :mod:`python ${file} ${argv}` where ``argv`` are the command
line arguments. You can retrieve them with ``sys.argv`` as in any Python script.

Content of ``mynode.py``:

.. code-block:: python

    import sys

    def main(argv, **kwargs):
        print(argv)

    if __name__ == "__main__":
        main(sys.argv)

Usage:

.. code-block:: bash

    $ gada mycomponent.mynode 1 2
    ['path/to/mynode.py', '1', '2']

.. note:: ``argv[0]`` is the Python script that is run.
