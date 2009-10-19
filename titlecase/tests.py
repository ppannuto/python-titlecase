#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for titlecase"""


import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../'))


from titlecase import titlecase


TEST_DATA = (
    (
        "Q&A with steve jobs: 'that's what happens in technology'",
        "Q&A With Steve Jobs: 'That's What Happens in Technology'"
    ),
    (
        "What is AT&T's problem?",
        "What Is AT&T's Problem?"
    ),
    (
        "Apple deal with AT&T falls through",
        "Apple Deal With AT&T Falls Through"
    ),
    (
        "this v that",
        "This v That"
    ),
    (
        "this v. that",
        "This v. That"
    ),
    (
        "this vs that",
        "This vs That"
    ),
    (
        "this vs. that",
        "This vs. That"
    ),
    (
        "The SEC's Apple probe: what you need to know",
        "The SEC's Apple Probe: What You Need to Know"
    ),
    (
        "'by the Way, small word at the start but within quotes.'",
        "'By the Way, Small Word at the Start but Within Quotes.'"
    ),
    (
        "Small word at end is nothing to be afraid of",
        "Small Word at End Is Nothing to Be Afraid Of"
    ),
    (
        "Starting Sub-Phrase With a Small Word: a Trick, Perhaps?",
        "Starting Sub-Phrase With a Small Word: A Trick, Perhaps?"
    ),
    (    
        "Sub-Phrase With a Small Word in Quotes: 'a Trick, Perhaps?'",
        "Sub-Phrase With a Small Word in Quotes: 'A Trick, Perhaps?'"
    ),
    (
        'sub-phrase with a small word in quotes: "a trick, perhaps?"',
        'Sub-Phrase With a Small Word in Quotes: "A Trick, Perhaps?"'
    ),
    (
        '"Nothing to Be Afraid of?"',
        '"Nothing to Be Afraid Of?"'
    ),
    (
        '"Nothing to be Afraid Of?"',
        '"Nothing to Be Afraid Of?"'    
    ),
    (   
        'a thing',
        'A Thing'
    ),
    (
        "2lmc Spool: 'gruber on OmniFocus and vapo(u)rware'",
        "2lmc Spool: 'Gruber on OmniFocus and Vapo(u)rware'"
    ),
    (
        'this is just an example.com',
        'This Is Just an example.com'
    ),
    (
        'this is something listed on del.icio.us',
        'This Is Something Listed on del.icio.us'
    ),
    (
        'iTunes should be unmolested',
        'iTunes Should Be Unmolested'
    ),
    (
        'reading between the lines of steve jobs’s ‘thoughts on music’',
        'Reading Between the Lines of Steve Jobs’s ‘Thoughts on Music’'
    ),
    (
        'seriously, ‘repair permissions’ is voodoo',
        'Seriously, ‘Repair Permissions’ Is Voodoo'
    ),
    (
        'generalissimo francisco franco: still dead; kieren McCarthy: still a jackass',
        'Generalissimo Francisco Franco: Still Dead; Kieren McCarthy: Still a Jackass'
    ),
    (
        "O'Reilly should be untouched",
        "O'Reilly Should Be Untouched"
    ),
    (
        "my name is o'reilly",
        "My Name Is O'Reilly"
    ),
    (
        "WASHINGTON, D.C. SHOULD BE FIXED BUT MIGHT BE A PROBLEM",
        "Washington, D.C. Should Be Fixed but Might Be a Problem"
    ),
    (
        "THIS IS ALL CAPS AND SHOULD BE ADDRESSED",
        "This Is All Caps and Should Be Addressed"
    )
)

class TitlecaseTests(unittest.TestCase):
    """Titlecase Tests"""
    
    def test_all_caps_regex(self):
        """Test - all capitals regex"""
        from titlecase import ALL_CAPS
        self.assertTrue(ALL_CAPS.match('THIS IS ALL CAPS'))

    def test_initials_regex(self):
        """Test - uppercase initals regex with A.B"""
        from titlecase import UC_INITIALS
        self.assertTrue(UC_INITIALS.match('A.B'))

    def test_initials_regex_2(self):
        """Test - uppercase initals regex with A.B."""
        from titlecase import UC_INITIALS
        self.assertTrue(UC_INITIALS.match('A.B.'))

    def test_initials_regex_3(self):
        """Test - uppercase initals regex with ABCD"""
        from titlecase import UC_INITIALS
        self.assertFalse(UC_INITIALS.match('ABCD'))

def io_test_generator(in_, out):
    """Builds basic tests"""
    def test(self):
        """Stub test"""
        return self.assertEqual(titlecase(in_), out)

    return test

    
if __name__ == "__main__":
    
    for i, test in enumerate(TEST_DATA):
        test_func = io_test_generator(test[0], test[1])
        test_func.__doc__ =  test[0]
        setattr(TitlecaseTests, "test_%s" % i, test_func)

    suite = unittest.TestLoader().loadTestsFromTestCase(TitlecaseTests)
    unittest.TextTestRunner(verbosity=2).run(suite)

