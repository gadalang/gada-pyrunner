.. -*- coding: utf-8 -*-
.. _python:

python Runner
=============

.. automodule:: gada_pyrunner.python

Full configuration
------------------

Based on Python package structure shown above:

.. code-block:: yaml

    nodes:
      mynode:
        runner: python
        [bin: python]
        file: ${comp_dir}/mynode.py

Parameters:

- ``bin``: Optional - Python bin to use in command line (default is ``python``)
- ``file``: Python script to run

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


Multiple Python versions
------------------------

Add the following to ``gada/config.yml``:

.. code-block:: yaml

    bins:
      python3.7: /path/to/python3.7.exe
      python3.8: /path/to/python3.8.exe

Now you can make your gada node either run with Python 3.7 or Python 3.8 by setting the right ``bin`` in ``config.yml``:

.. code-block:: yaml

    nodes:
      mynode:
        runner: python
        bin: python3.8
        file: mynode.py

Content of ``mynode.py``:

.. code-block:: python

    import sys

    def main(**kwargs):
        print(sys.version)

    if __name__ == "__main__":
        main()

Usage:

.. code-block:: bash

    $ gada mycomponent.mynode
    3.8
