=============
ckanext-odn
=============

Estensione per OpenDataNetwork.

Fornisce 2 plugin:

- ``odn_theme``: customizzazione GUI
- ``odn_harvest``: ridefinisce alcuni comportamenti dell'harvester spaziale.


------------
Requirements
------------

Sviluppato e testato su CKAN 2.5.2.

Richiede che sia installato il plugin *spatial-harvester*.


------------
Installation
------------

To install *ckanext-odn*:

1. Activate your CKAN virtual environment, for example::

     . /usr/lib/ckan/default/bin/activate

2. Install the *ckanext-odn* Python package into your virtual environment::

     pip install ckanext-odn

3. Add ``odn_theme`` and ``odn_harvest`` to the ``ckan.plugins`` setting in your CKAN
   config file (by default the config file is located at
   ``/etc/ckan/default/production.ini``).

4. Restart CKAN. For example if you've deployed CKAN with Apache on Ubuntu::

     sudo service apache2 reload


---------------
Config Settings
---------------

- ``odn.map_link``

  The URL where the map link in the home page should point to. E.g.::
      
     odn.map_link = http://www.opendatanetwork.it/tolomeo/html/servizi/cerco/cerco.html?paramPreset=Cerco
   

------------------------
Development Installation
------------------------

To install *ckanext-odn* for development, activate your CKAN virtualenv and
do::

    git clone https://github.com/geosolution-it/ckanext-odn.git
    cd ckanext-odn
    python setup.py develop
    pip install -r dev-requirements.txt

