#!/usr/bin/env python
# encoding: utf-8

"""
titlecase.py v0.1
Original Perl version by: John Gruber http://daringfireball.net/ 10 May 2008
Python port by Stuart Colville http://muffinresearch.co.uk
License: http://www.opensource.org/licenses/mit-license.php
"""

import unittest
import sys
import re


def titlecase(text):

    """
    This filter changes all words to Title Caps, and attempts to be clever
    about *un*capitalizing small words like a/an/the in the input.

    The list of "small words" which are not capped comes from
    the New York Times Manual of Style, plus 'vs' and 'v'.
    """

    small = '(a|an|and|as|at|but|by|en|for|if \
            |in|of|on|or|the|to|v\.?|via|vs\.?)'
    punct = "([!\"#$%&'()*+,-./:;?@[\\\\\\]_`{|}~]*)"
    start_words = re.compile(r'^%s%s\b' % (punct, small), re.I)
    end_words = re.compile(r'\b%s%s$' % (small, punct), re.I)
    small_words = re.compile(r'\b%s\b' % small,  re.I)
    inline_period = re.compile(r'[a-zA-Z]\.[a-zA-Z]')
    words = re.compile(r"([A-Za-z][a-z.'“]*)")
    plural = re.compile(r"(['’])S\b")
    ampersand = re.compile(r'\b(AT&T|Q&A)\b', re.I)
    versus = re.compile(r" V(s?)\. ")
    pieces = re.compile(r'( [:.;?!][ ] | (?:[ ]|^)["“] )', re.X)

    parts = re.split(pieces, text)

    lines = []
    for part in parts:
        line = words.sub(
            lambda submatch: re.match(inline_period, submatch.group(0))
                and submatch.group(0)
                or submatch.group(0).capitalize()
        , part)
        line = small_words.sub(
            lambda small_word: small_word.group(0).lower(), line
        )
        line = start_words.sub(
            lambda start: '%s%s' % (start.group(1), start.group(2).capitalize())
        , line)
        line = end_words.sub(lambda end: end.group(0).capitalize(), line)

        lines.append(line)

    line = ''.join(lines)
    line = versus.sub(r" v\1. ", line) # vs vs. v and v. special case
    line = plural.sub(r'\1s', line)  # plurals
    line = ampersand.sub(lambda m: m.group(0).upper(), line) # AT&T and Q&A

    return line

class TitlecaseTests(unittest.TestCase):
    
    """ Tests to ensure titlecase follows all of the rules """

    def test_q_and_a(self):
        """ Testing: Q&A With Steve Jobs: 'That's What Happens In 
        Technology' """
        text = titlecase(
            "Q&A With Steve Jobs: 'That's What Happens In Technology'"
        )
        result = "Q&A With Steve Jobs: 'That's What Happens in Technology'"
        self.assertEqual(text, result, "%s should be: %s" % (text, result, ))

    def test_at_and_t(self):
        """ Testing: What Is AT&T's Problem? """
        text = titlecase("What Is AT&T's Problem?")
        result = "What Is AT&T's Problem?"
        self.assertEqual(text, result, "%s should be: %s" % (text, result, ))

    def test_apple_deal(self):
        """ Testing: Apple Deal With AT&T Falls Through """
        text = titlecase("Apple Deal With AT&T Falls Through")
        result = "Apple Deal With AT&T Falls Through"
        self.assertEqual(text, result, "%s should be: %s" % (text, result, ))

    def test_this_v_that(self):
        """ Testing: this v that """
        text = titlecase("this v that")
        result = "This v That"
        self.assertEqual(text, result, "%s should be: %s" % (text, result, ))

    def test_this_v_that2(self):
        """ Testing: this v. that """
        text = titlecase("this v. that")
        result = "This v. That"
        self.assertEqual(text, result, "%s should be: %s" % (text, result, ))

    def test_this_vs_that(self):
        """ Testing: this vs that """
        text = titlecase("this vs that")
        result = "This vs That"
        self.assertEqual(text, result, "%s should be: %s" % (text, result, ))

    def test_this_vs_that2(self):
        """ Testing: this vs. that """
        text = titlecase("this vs. that")
        result = "This vs. That"
        self.assertEqual(text, result, "%s should be: %s" % (text, result, ))

    def test_apple_sec(self):
        """ Testing: The SEC's Apple Probe: What You Need to Know """
        text = titlecase("The SEC's Apple Probe: What You Need to Know")
        result = "The SEC's Apple Probe: What You Need to Know"
        self.assertEqual(text, result, "%s should be: %s" % (text, result, ))

    def test_small_word_quoted(self):
        """ Testing: 'by the Way, small word at the start but within 
        quotes.'"""
        text = titlecase(
            "'by the Way, small word at the start but within quotes.'"
        )
        result = "'By the Way, Small Word at the Start but Within Quotes.'"
        self.assertEqual(text, result, "%s should be: %s" % (text, result, ))

    def test_small_word_end(self):
        """ Testing: Small word at end is nothing to be afraid of """
        text = titlecase("Small word at end is nothing to be afraid of")
        result = "Small Word at End Is Nothing to Be Afraid Of"
        self.assertEqual(text, result, "%s should be: %s" % (text, result, ))

    def test_sub_phrase_small_word(self):
        """ Testing: Starting Sub-Phrase With a Small Word: a Trick, 
        Perhaps?
        """
        text = titlecase(
            "Starting Sub-Phrase With a Small Word: a Trick, Perhaps?"
        )
        result = "Starting Sub-Phrase With a Small Word: A Trick, Perhaps?"
        self.assertEqual(text, result, "%s should be: %s" % (text, result, ))

    def test_small_word_quotes(self):
        """ Testing: Sub-Phrase With a Small Word in Quotes: 'a Trick, 
        Perhaps?' """
        text = titlecase(
            "Sub-Phrase With a Small Word in Quotes: 'a Trick, Perhaps?'"
        )
        result = "Sub-Phrase With a Small Word in Quotes: 'A Trick, Perhaps?'"
        self.assertEqual(text, result, "%s should be: %s" % (text, result, ))

    def test_small_word_double_quotes(self):
        """ Testing: Sub-Phrase With a Small Word in Quotes: \"a Trick, 
        Perhaps?\" """
        text = titlecase(
            'Sub-Phrase With a Small Word in Quotes: "a Trick, Perhaps?"'
        )
        result = 'Sub-Phrase With a Small Word in Quotes: "A Trick, Perhaps?"'
        self.assertEqual(text, result, "%s should be: %s" % (text, result, ))

    def test_nothing_to_be_afraid_of(self):
        """ Testing: \"Nothing to Be Afraid of?\" """
        text = titlecase('"Nothing to Be Afraid of?"')
        result = '"Nothing to Be Afraid Of?"'
        self.assertEqual(text, result, "%s should be: %s" % (text, result, ))

    def test_nothing_to_be_afraid_of2(self):
        """ Testing: \"Nothing to Be Afraid Of?\" """
        text = titlecase('"Nothing to Be Afraid Of?"')
        result = '"Nothing to Be Afraid Of?"'
        self.assertEqual(text, result, "%s should be: %s" % (text, result, ))

    def test_a_thing(self):
        """ Testing: a thing """
        text = titlecase('a thing')
        result = 'A Thing'
        self.assertEqual(text, result, "%s should be: %s" % (text, result, ))

    def test_vapourware(self):
        """ Testing: '2lmc Spool: 'Gruber on OmniFocus and Vapo(u)rware' """
        text = titlecase(
            "'2lmc Spool: 'Gruber on OmniFocus and Vapo(u)rware'"
        )
        result = "2lmc Spool: 'Gruber on OmniFocus and Vapo(u)rware'"
        self.assertEqual(text, result, "%s should be: %s" % (text, result, ))

if __name__ == '__main__':    
    if not sys.stdin.isatty():
        for line in sys.stdin:
            try:
                print titlecase(line),
            except:
                pass
    else:
        suite = unittest.TestLoader().loadTestsFromTestCase(TitlecaseTests)
        unittest.TextTestRunner(verbosity=2).run(suite)
