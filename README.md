# packaging_template
Simple example of how to package a python project into an installable module

setup.py
- points to entry points a.k.a where the scripts are stored
- installs necessary packages from requirements.txt
- run with python setup.py install

requirements.txt
- lists necessary packages
- can simply list packages e.g. numpy
- pip freeze method not recommended 

__init__.py
- allows all python modules within the same directory to be called

.gitignore
- ignores files that don't need to be interpreted e.g. __pycache__

Useful command line arguments:
- touch <filename> = creates file
- vi <filename> = allows you to edit file
  - insert to edit, escape to get out of edit mode
  - :wq to save changes 
- ipython = command shell for computing in multiple languages
