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

Test
----

You can run the unit tests with the following command.

.. code-block:: bash

    python setup.py test

