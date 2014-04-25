Titlecase
=========

This filter changes all words to Title Caps, and attempts to be clever
about *un*\capitalizing SMALL words like a/an/the in the input.

The list of "SMALL words" which are not capped comes from
the New York Times Manual of Style, plus 'vs' and 'v'.

This is a fork of [Stuart Colville's titlecase.py][tc_home], which was in turn
a port of [John Gruber's titlecase.pl][tc_perl].

The purpose of this fork is to update the package to support Python 3 as well
as provide a maintained version of this utility. Issues or better pull requests
are welcome.

Usage
-----

To use it is as simple as:

```
>>> from titlecase import titlecase
>>> titlecase('a thing')
'A Thing'
```


[tc_home]: https://muffinresearch.co.uk/titlecasepy-titlecase-in-python/
[tc_lp]: https://launchpad.net/titlecase.py
[tc_perl]: http://daringfireball.net/2008/05/title_case
