Titlecase
=========

.. image:: https://travis-ci.org/ppannuto/python-titlecase.svg?branch=master
    :target: https://travis-ci.org/ppannuto/python-titlecase
.. image:: https://coveralls.io/repos/github/ppannuto/python-titlecase/badge.svg?branch=master
    :target: https://coveralls.io/github/ppannuto/python-titlecase?branch=master

This filter changes all words to Title Caps, and attempts to be clever
about SMALL words like a/an/the in the input.

The list of "SMALL words" which are not capped comes from the New York
Times Manual of Style, plus some others like 'vs' and 'v'.

This is a resurrection of `Stuart Colville's
titlecase.py <https://muffinresearch.co.uk/titlecasepy-titlecase-in-python/>`__,
which was in turn a port of `John Gruber's
titlecase.pl <http://daringfireball.net/2008/05/title_case>`__.

Issues, updates, pull requests, etc should be directed
`to github <https://github.com/ppannuto/python-titlecase>`__.


Installation
------------

The easiest method is to simply use pip:

::

    (sudo) pip install titlecase


Usage
-----

Titlecase provides only one function, simply:

.. code-block:: python

    >>> from titlecase import titlecase
    >>> titlecase('a thing')
    'A Thing'

A callback function may also be supplied, which will be called for every word:

.. code-block:: python

    >>> def abbreviations(word, **kwargs):
    ...   if word.upper() in ('TCP', 'UDP'):
    ...     return word.upper()
    ...
    >>> titlecase.titlecase('a simple tcp and udp wrapper', callback=abbreviations)
    'A Simple TCP and UDP Wrapper'

The callback function is supplied with an ``all_caps`` keyword argument, indicating
whether the entire line of text was entirely capitalized. Returning ``None`` from
the callback function will allow titlecase to process the word as normal.


Command Line Usage
------------------

Titlecase also provides a command line utility ``titlecase``:

.. code-block:: python

    $ titlecase make me a title
    Make Me a Title
    $ echo "Can pipe and/or whatever else" | titlecase
    Can Pipe and/or Whatever Else
    # Or read/write files:
    $ titlecase -f infile -o outfile

