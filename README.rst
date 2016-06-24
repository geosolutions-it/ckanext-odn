.. You should enable this project on travis-ci.org and coveralls.io to make
   these badges work. The necessary Travis and Coverage config files have been
   generated for you.

.. image:: https://travis-ci.org/etj/ckanext-odn.svg?branch=master
    :target: https://travis-ci.org/etj/ckanext-odn

.. image:: https://coveralls.io/repos/etj/ckanext-odn/badge.svg
  :target: https://coveralls.io/r/etj/ckanext-odn

.. image:: https://pypip.in/download/ckanext-odn/badge.svg
    :target: https://pypi.python.org/pypi//ckanext-odn/
    :alt: Downloads

.. image:: https://pypip.in/version/ckanext-odn/badge.svg
    :target: https://pypi.python.org/pypi/ckanext-odn/
    :alt: Latest Version

.. image:: https://pypip.in/py_versions/ckanext-odn/badge.svg
    :target: https://pypi.python.org/pypi/ckanext-odn/
    :alt: Supported Python versions

.. image:: https://pypip.in/status/ckanext-odn/badge.svg
    :target: https://pypi.python.org/pypi/ckanext-odn/
    :alt: Development Status

.. image:: https://pypip.in/license/ckanext-odn/badge.svg
    :target: https://pypi.python.org/pypi/ckanext-odn/
    :alt: License

=============
ckanext-odn
=============

Estensione per OpeDataNetwork.

Fornisce 2 plugin:
- odn_theme: customizzazione GUI
- odn_harvest: ridefinisce alcuni comportamenti dell'harvester spaziale.'


------------
Requirements
------------

Sviluppato e testato su CKAN 2.5.2.

Richiede che sia installato il plugin spatial-harvester.


------------
Installation
------------

To install ckanext-odn:

1. Activate your CKAN virtual environment, for example::

     . /usr/lib/ckan/default/bin/activate

2. Install the ckanext-odn Python package into your virtual environment::

     pip install ckanext-odn

3. Add ``odn_theme`` and ``adn_harvest`` to the ``ckan.plugins`` setting in your CKAN
   config file (by default the config file is located at
   ``/etc/ckan/default/production.ini``).

4. Restart CKAN. For example if you've deployed CKAN with Apache on Ubuntu::

     sudo service apache2 reload


---------------
Config Settings
---------------

Document any optional config settings here. For example::

    # The minimum number of hours to wait before re-checking a resource
    # (optional, default: 24).
    ckanext.odn.some_setting = some_default_value


------------------------
Development Installation
------------------------

To install ckanext-odn for development, activate your CKAN virtualenv and
do::

    git clone https://github.com/geosolution-it/ckanext-odn.git
    cd ckanext-odn
    python setup.py develop
    pip install -r dev-requirements.txt


-----------------
Running the Tests
-----------------

To run the tests, do::

    nosetests --nologcapture --with-pylons=test.ini

To run the tests and produce a coverage report, first make sure you have
coverage installed in your virtualenv (``pip install coverage``) then run::

    nosetests --nologcapture --with-pylons=test.ini --with-coverage --cover-package=ckanext.odn --cover-inclusive --cover-erase --cover-tests


---------------------------------
Registering ckanext-odn on PyPI
---------------------------------

ckanext-odn should be availabe on PyPI as
https://pypi.python.org/pypi/ckanext-odn. If that link doesn't work, then
you can register the project on PyPI for the first time by following these
steps:

1. Create a source distribution of the project::

     python setup.py sdist

2. Register the project::

     python setup.py register

3. Upload the source distribution to PyPI::

     python setup.py sdist upload

4. Tag the first release of the project on GitHub with the version number from
   the ``setup.py`` file. For example if the version number in ``setup.py`` is
   0.0.1 then do::

       git tag 0.0.1
       git push --tags


----------------------------------------
Releasing a New Version of ckanext-odn
----------------------------------------

ckanext-odn is availabe on PyPI as https://pypi.python.org/pypi/ckanext-odn.
To publish a new version to PyPI follow these steps:

1. Update the version number in the ``setup.py`` file.
   See `PEP 440 <http://legacy.python.org/dev/peps/pep-0440/#public-version-identifiers>`_
   for how to choose version numbers.

2. Create a source distribution of the new version::

     python setup.py sdist

3. Upload the source distribution to PyPI::

     python setup.py sdist upload

4. Tag the new release of the project on GitHub with the version number from
   the ``setup.py`` file. For example if the version number in ``setup.py`` is
   0.0.2 then do::

       git tag 0.0.2
       git push --tags
