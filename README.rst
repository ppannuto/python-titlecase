Titlecase
=========

This filter changes all words to Title Caps, and attempts to be clever
about *un*\ SMALL words like a/an/the in the input.

The list of "SMALL words" which are not capped comes from the New York
Times Manual of Style, plus 'vs' and 'v'.

This is a fork of `Stuart Colville's
titlecase.py <https://muffinresearch.co.uk/titlecasepy-titlecase-in-python/>`__,
which was in turn a port of `John Gruber's
titlecase.pl <http://daringfireball.net/2008/05/title_case>`__.

The purpose of this fork is to update the package to support Python 3 as
well as provide a maintained version of this utility. Issues or better
pull requests are welcome.

Usage
-----

To use it is as simple as:

::

    >>> from titlecase import titlecase
    >>> titlecase('a thing')
    'A Thing'

