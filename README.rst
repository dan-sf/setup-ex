Setup Example
=============

This is an example template for creating Python packages using Python's
setuptools. This package includes a basic setup.py file, with a few sample
classes and tests. This can be used as a starting point for developing a Python
package from scratch.

Install
-------

This package can be installed with or without a virtual environment.

.. code-block:: bash

    git clone https://github.com/dan-sf/setup-ex
    cd setup-ex
    # Optionally create a virtual env
    virtualenv /PATH/TO/VENV/setup_ex
    source /PATH/TO/VENV/setup_ex/bin/activate
    pip install -e .
    # Run the entry point
    se
    This is an entry point, let's call our custom API class
    This is a custom api

Docker
------

You can optionally use Docker to build and test this code. The Docker code is
meant to serve as an example of how to use Docker for python development
allowing for live code edits on the host machine taking immediate effect on the
docker container without rebuilding the image.

Test
----

You can run the unit tests with the following command.

.. code-block:: bash

    python setup.py test

