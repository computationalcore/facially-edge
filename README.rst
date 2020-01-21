facially-edge
================

.. image:: https://travis-ci.org/computationalcore/facially-edge.svg?branch=master
    :target: https://travis-ci.org/computationalcore/facially-edge
    
.. image:: https://coveralls.io/repos/github/computationalcore/facially-edge/badge.svg?branch=master
    :target: https://coveralls.io/github/computationalcore/facially-edge?branch=master

.. image:: https://img.shields.io/lgtm/grade/python/g/computationalcore/facially-edge.svg?logo=lgtm&logoWidth=18
    :target: https://lgtm.com/projects/g/computationalcore/facially-edge/context:python



(Work in progress)
An edge app, part of Facially-targeted Ads Platform, that is responsible for running a 
neural network model for inference data based on facial features, estimate age, gender, 
emotions and head-pose, send this data to a web service in order to get the appropriate 
ads for that particular audience, and display it on the screen. 
The app will run on a device with a video camera attached, and internally will use 
Intel® Distribution of OpenVINO™ toolkit for DNN inference.

Requirements
------------

Python 3.5+.

.. note::

    Because `Python 2.7 supports ended January 1, 2020 <https://pythonclock.org/>`_, new projects
    should consider supporting Python 3 only, which is simpler than trying to support both.
    As a result, support for Python 2.7 in this example project has been dropped.

Windows Support
---------------

Summary: On Windows, use ``py`` instead of ``python3`` for many of the examples in this
documentation.

This package fully supports Windows, along with Linux and macOS, but Python is typically
`installed differently on Windows <https://docs.python.org/3/using/windows.html>`_.
Windows users typically access Python through the
`py <https://www.python.org/dev/peps/pep-0397/>`_ launcher rather than a ``python3``
link in their ``PATH``. Within a virtual environment, all platforms operate the same and use a
``python`` link to access the Python version used in that virtual environment.


Installation
------------

To install and run the program without development environment folloe the instruction

Create and start the virtual environment (Check section "Virtual Environments"  for more details)
.. code:: bash

    $ python3 -m venv venv
    $ source venv/bin/activate

Install the requirements
    $ pip -r requirements.txt

To execute the cli (example)
.. code:: bash

    $ cd src
    $ python -m facially.cli -s World

Packaging
---------

This project is designed as a Python package, meaning that it can be bundled up and redistributed
as a single compressed file.

Packaging is configured by:

- ``setup.py``

- ``MANIFEST.in``

Source Distribution
^^^^^^^^^^^^^^^^^^^

To package the project as a
`source distribution <https://docs.python.org/3/distutils/sourcedist.html>`_:

.. code-block:: bash

    $ python3 setup.py sdist

This will generate ``dist/facially-0.0.1.tar.gz``.

Dependencies
------------

Dependencies are defined in:

- ``requirements.in``

- ``requirements.txt``

- ``dev-requirements.in``

- ``dev-requirements.txt``

Virtual Environments
^^^^^^^^^^^^^^^^^^^^

It is best practice during development to create an isolated
`Python virtual environment <https://docs.python.org/3/library/venv.html>`_ using the
``venv`` standard library module. This will keep dependant Python packages from interfering
with other Python projects on your system.

On \*Nix:

.. code-block:: bash

    $ python3 -m venv venv
    $ source venv/bin/activate

On Windows ``cmd``:

.. code-block:: bash

    > py -m venv venv
    > venv\Scripts\activate.bat

Once activated, it is good practice to update ``pip`` to the latest version.

.. code-block:: bash

    (venv) $ pip install --upgrade pip

(Applications Only) Locking Dependencies
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This project uses `pip-tools <https://github.com/jazzband/pip-tools>`_ to lock project
dependencies and create reproducible virtual environments.

**Note:** *Library* projects should not lock their ``requirements.txt``. Since ``python-blueprint``
also has a CLI application, this end-user application example is used to demonstrate how to
lock application dependencies.

To update dependencies:

.. code-block:: bash

    (venv) $ pip install pip-tools
    (venv) $ pip-compile --upgrade
    (venv) $ pip-compile --upgrade dev-requirements.in

After upgrading dependencies, run the unit tests as described in the `Unit Testing`_ section
to ensure that none of the updated packages caused incompatibilities in the current project.

Syncing Virtual Environments
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To cleanly install your dependencies into your virtual environment:

.. code-block:: bash

    (venv) $ pip-sync requirements.txt dev-requirements.txt

Testing
-------

Automated testing is performed using `tox <https://tox.readthedocs.io/en/latest/index.html>`_.
tox will automatically create virtual environments based on ``tox.ini`` for unit testing,
PEP8 style guide checking, and documentation generation.

.. code-block:: bash

    # Install tox (only needed once).
    $ python3 -m pip install tox

    # Run all environments.
    #   To only run a single environment, specify it like: -e pep8
    $ tox

Unit Testing
^^^^^^^^^^^^

Unit testing is performed with `pytest <https://pytest.org/>`_. pytest has become the defacto
Python unit testing framework. Some key advantages over the built in
`unittest <https://docs.python.org/3/library/unittest.html>`_ module are:

#. Significantly less boilerplate needed for tests.

#. PEP8 compliant names (e.g. ``pytest.raises()`` instead of ``self.assertRaises()``).

#. Vibrant ecosystem of plugins.

pytest will automatically discover and run tests by recursively searching for folders and ``.py``
files prefixed with ``test`` for any functions prefixed by ``test``.

The ``tests`` folder is created as a Python package (i.e. there is an ``__init__.py`` file
within it) because this helps ``pytest`` uniquely namespace the test files. Without this,
two test files cannot be named the same, even if they are in different sub-directories.

Code coverage is provided by the `pytest-cov <https://pytest-cov.readthedocs.io/en/latest/>`_
plugin.

When running a unit test tox environment (e.g. ``tox``, ``tox -e py37``, etc.), a data file
(e.g. ``.coverage.py37``) containing the coverage data is generated. This file is not readable on
its own, but when the ``coverage`` tox environment is run (e.g. ``tox`` or ``tox -e -coverage``),
coverage from all unit test environments is combined into a single data file and an HTML report is
generated in the ``htmlcov`` folder showing each source file and which lines were executed during
unit testing. Open ``htmlcov/index.html`` in a web browser to view the report. Code coverage 
reports help identify areas of the project that are currently not tested.

Code coverage is configured in the ``.coveragerc`` file.


Code Style Checking
^^^^^^^^^^^^^^^^^^^

`PEP8 <https://www.python.org/dev/peps/pep-0008/>`_ is the universally accepted style
guide for Python code. PEP8 code compliance is verified using `flake8 <http://flake8.pycqa.org/>`_.
flake8 is configured in the ``[flake8]`` section of ``tox.ini``. Three extra flake8 plugins
are also included:

- ``pep8-naming``: Ensure functions, classes, and variables are named with correct casing.
- ``flake8-quotes``: Ensure that ``' '`` style string quoting is used consistently.
- ``flake8-import-order``: Ensure consistency in the way imports are grouped and sorted.

Project Structure
-----------------

Traditionally, Python projects place the source for their packages in the root of the project
structure, like:

.. code-block::

    root_folder
    ├── facially
    │   ├── __init__.py
    │   ├── cli.py
    │   └── lib.py
    ├── tests
    │   ├── __init__.py
    │   └── test_generate.py
    ├── tox.ini
    └── setup.py

However, this structure is `known
<https://docs.pytest.org/en/latest/goodpractices.html#tests-outside-application-code>`_ to have bad
interactions with ``pytest`` and ``tox``, two standard tools maintaining Python projects. The
fundamental issue is that tox creates an isolated virtual environment for testing. By installing
the distribution into the virtual environment, ``tox`` ensures that the tests pass even after the
distribution has been packaged and installed, thereby catching any errors in packaging and
installation scripts, which are common. Having the Python packages in the project root subverts
this isolation for two reasons:

#. Calling ``python`` in the project root (for example, ``python -m pytest tests/``) `causes Python
   to add the current working directory
   <https://docs.pytest.org/en/latest/pythonpath.html#invoking-pytest-versus-python-m-pytest>`_
   (the project root) to ``sys.path``, which Python uses to find modules. Because the source
   package ``facially`` is in the project root, it shadows the ``facially`` package installed in the tox
   environment.

#. Calling ``pytest`` directly anywhere that it can find the tests will also add the project root
   to ``sys.path`` if the ``tests`` folder is a a Python package (that is, it contains a
   ``__init__.py`` file). `pytest adds all folders containing packages
   <https://docs.pytest.org/en/latest/goodpractices.html#conventions-for-python-test-discovery>`_
   to ``sys.path`` because it imports the tests like regular Python modules.

In order to properly test the project, the source packages must not be on the Python path. To
prevent this, there are three possible solutions:

#. Remove the ``__init__.py`` file from ``tests`` and run ``pytest`` directly as a tox command.

#. Remove the ``__init__.py`` file from tests and change the working directory of
   ``python -m pytest`` to ``tests``.

#. Move the source packages to a dedicated ``src`` folder.

The dedicated ``src`` directory is the `recommended solution
<https://docs.pytest.org/en/latest/pythonpath.html#test-modules-conftest-py-files-inside-packages>`_
by ``pytest`` when using tox and the solution this blueprint promotes because it is the least
brittle even though it deviates from the traditional Python project structure. It results is a
directory structure like:

.. code-block::

    root_folder
    ├── src
    │   └── facially
    │       ├── __init__.py
    │       ├── cli.py
    │       └── lib.py
    ├── tests
    │   ├── __init__.py
    │   └── test_generate.py
    ├── tox.ini
    └── setup.py

Licensing
---------

Licensing for the project is defined in:

- ``LICENSE.txt``

- ``setup.py``

This project uses a common permissive license, the MIT license.
