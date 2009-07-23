#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from titlecase import titlecase


class TitlecaseTests(unittest.TestCase):

    """Tests to ensure titlecase follows all of the rules"""

    def test_q_and_a(self):
        """Testing: Q&A With Steve Jobs: 'That's What Happens In Technology' """
        text = titlecase(
            "Q&A with steve jobs: 'that's what happens in technology'"
        )
        result = "Q&A With Steve Jobs: 'That's What Happens in Technology'"
        self.assertEqual(text, result, "%s should be: %s" % (text, result, ))

    def test_at_and_t(self):
        """Testing: What Is AT&T's Problem?"""

        text = titlecase("What is AT&T's problem?")
        result = "What Is AT&T's Problem?"
        self.assertEqual(text, result, "%s should be: %s" % (text, result, ))

    def test_apple_deal(self):
        """Testing: Apple Deal With AT&T Falls Through"""

        text = titlecase("Apple deal with AT&T falls through")
        result = "Apple Deal With AT&T Falls Through"
        self.assertEqual(text, result, "%s should be: %s" % (text, result, ))

    def test_this_v_that(self):
        """Testing: this v that"""
        text = titlecase("this v that")
        result = "This v That"
        self.assertEqual(text, result, "%s should be: %s" % (text, result, ))

    def test_this_v_that2(self):
        """Testing: this v. that"""

        text = titlecase("this v. that")
        result = "This v. That"
        self.assertEqual(text, result, "%s should be: %s" % (text, result, ))

    def test_this_vs_that(self):
        """Testing: this vs that"""

        text = titlecase("this vs that")
        result = "This vs That"
        self.assertEqual(text, result, "%s should be: %s" % (text, result, ))

    def test_this_vs_that2(self):
        """Testing: this vs. that"""

        text = titlecase("this vs. that")
        result = "This vs. That"
        self.assertEqual(text, result, "%s should be: %s" % (text, result, ))

    def test_apple_sec(self):
        """Testing: The SEC's Apple Probe: What You Need to Know"""

        text = titlecase("The SEC's Apple Probe: What You Need to Know")
        result = "The SEC's Apple Probe: What You Need to Know"
        self.assertEqual(text, result, "%s should be: %s" % (text, result, ))

    def test_small_word_quoted(self):
        """Testing: 'by the Way, Small word at the start but within quotes.'"""

        text = titlecase(
            "'by the Way, small word at the start but within quotes.'"
        )
        result = "'By the Way, Small Word at the Start but Within Quotes.'"
        self.assertEqual(text, result, "%s should be: %s" % (text, result, ))

    def test_small_word_end(self):
        """Testing: Small word at end is nothing to be afraid of"""

        text = titlecase("Small word at end is nothing to be afraid of")
        result = "Small Word at End Is Nothing to Be Afraid Of"
        self.assertEqual(text, result, "%s should be: %s" % (text, result, ))

    def test_sub_phrase_small_word(self):
        """Testing: Starting Sub-Phrase With a Small Word: a Trick, Perhaps?"""

        text = titlecase(
            "Starting Sub-Phrase With a Small Word: a Trick, Perhaps?"
        )
        result = "Starting Sub-Phrase With a Small Word: A Trick, Perhaps?"
        self.assertEqual(text, result, "%s should be: %s" % (text, result, ))

    def test_small_word_quotes(self):
        """Testing: Sub-Phrase With a Small Word in Quotes: 'a Trick..."""

        text = titlecase(
            "Sub-Phrase With a Small Word in Quotes: 'a Trick, Perhaps?'"
        )
        result = "Sub-Phrase With a Small Word in Quotes: 'A Trick, Perhaps?'"
        self.assertEqual(text, result, "%s should be: %s" % (text, result, ))

    def test_small_word_double_quotes(self):
        """Testing: Sub-Phrase With a Small Word in Quotes: \"a Trick..."""
        text = titlecase(
            'Sub-Phrase With a Small Word in Quotes: "a Trick, Perhaps?"'
        )
        result = 'Sub-Phrase With a Small Word in Quotes: "A Trick, Perhaps?"'
        self.assertEqual(text, result, "%s should be: %s" % (text, result, ))

    def test_nothing_to_be_afraid_of(self):
        """Testing: \"Nothing to Be Afraid of?\""""
        text = titlecase('"Nothing to Be Afraid of?"')
        result = '"Nothing to Be Afraid Of?"'
        self.assertEqual(text, result, "%s should be: %s" % (text, result, ))

    def test_nothing_to_be_afraid_of2(self):
        """Testing: \"Nothing to Be Afraid Of?\""""

        text = titlecase('"Nothing to be Afraid Of?"')
        result = '"Nothing to Be Afraid Of?"'
        self.assertEqual(text, result, "%s should be: %s" % (text, result, ))

    def test_a_thing(self):
        """Testing: a thing"""

        text = titlecase('a thing')
        result = 'A Thing'
        self.assertEqual(text, result, "%s should be: %s" % (text, result, ))

    def test_vapourware(self):
        """Testing: 2lmc Spool: 'Gruber on OmniFocus and Vapo(u)rware'"""
        text = titlecase(
            "2lmc Spool: 'gruber on OmniFocus and vapo(u)rware'"
        )
        result = "2lmc Spool: 'Gruber on OmniFocus and Vapo(u)rware'"
        self.assertEqual(text, result, "%s should be: %s" % (text, result, ))

    def test_domains(self):
        """Testing: this is just an example.com"""
        text = titlecase('this is just an example.com')
        result = 'This Is Just an example.com'
        self.assertEqual(text, result, "%s should be: %s" % (text, result, ))

    def test_domains2(self):
        """Testing: this is something listed on an del.icio.us"""

        text = titlecase('this is something listed on del.icio.us')
        result = 'This Is Something Listed on del.icio.us'
        self.assertEqual(text, result, "%s should be: %s" % (text, result, ))

    def test_itunes(self):
        """Testing: iTunes should be unmolested"""

        text = titlecase('iTunes should be unmolested')
        result = 'iTunes Should Be Unmolested'
        self.assertEqual(text, result, "%s should be: %s" % (text, result, ))

    def test_thoughts_on_music(self):
        """Testing: Reading Between the Lines of Steve Jobs’s..."""

        text = titlecase(
            'Reading between the lines of steve jobs’s ‘thoughts on music’'
        )
        result = 'Reading Between the Lines of Steve Jobs’s ‘Thoughts on '\
            'Music’'
        self.assertEqual(text, result, "%s should be: %s" % (text, result, ))

    def test_repair_perms(self):
        """Testing: Seriously, ‘Repair Permissions’ Is Voodoo"""

        text = titlecase('seriously, ‘repair permissions’ is voodoo')
        result = 'Seriously, ‘Repair Permissions’ Is Voodoo'
        self.assertEqual(text, result, "%s should be: %s" % (text, result, ))

    def test_generalissimo(self):
        """Testing: Generalissimo Francisco Franco..."""

        text = titlecase(
            'generalissimo francisco franco: still dead; kieren McCarthy: '\
                'still a jackass'
        )
        result = 'Generalissimo Francisco Franco: Still Dead; Kieren '\
            'McCarthy: Still a Jackass'
        self.assertEqual(text, result, "%s should be: %s" % (text, result, ))


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TitlecaseTests)
    unittest.TextTestRunner(verbosity=2).run(suite)

