Titlecase
=========

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

::

    >>> from titlecase import titlecase
    >>> titlecase('a thing')
    'A Thing'

