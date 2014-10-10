# MOOC Aggregator Restful API

This project is a restful api over various MOOC APIs. This restful api can be
used to create one's own online course aggregator app

| Build Status |
| ------------ |
| [![Build Status](https://travis-ci.org/ueg1990/mooc_aggregator_restful_api.svg?branch=master)](https://travis-ci.org/ueg1990/mooc_aggregator_restful_api)|

# Tests

To run individual tests, under the pypoker parent folder,

    $ python -m unittest tests.<module name>

To run all the tests, under the pypoker parent folder, just do:

    $ python -m unittest discover tests -v

To run all tests using nose,

    $ nosetests -v tests

To run all tests using nose and coverage,

    $ nosetests -v --with-coverage --cover-package=mooc_aggregator_restful_api --cover-inclusive --cover-erase tests

# PEP 8 Test

Whole project:

    $ pep8 --exclude=*.txt,*.md,*.pyc,.svn,CVS,.bzr,.hg,.git,__pycache__ *

A specific file:

    $ pep8 --exclude=*.txt,*.md,*.pyc,.svn,CVS,.bzr,.hg,.git,__pycache__ <path_to_file>

# Author

Usman Ehtesham Gul - <uehtesham90@gmail.com>
