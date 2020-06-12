#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for titlecase"""

from __future__ import print_function, unicode_literals

import os
import sys
import tempfile
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../'))

from titlecase import titlecase, set_small_word_list


# (executed by `test_input_output` below)
TEST_DATA = (
    (
        "",
        ""
    ),
    (
        "word/word",
        "Word/Word"
    ),
    (
        "a title and/or string",
        "A Title and/or String"
    ),
    (
        "dance with me/let’s face the music and dance",
        "Dance With Me/Let’s Face the Music and Dance"
    ),
    (
        "34th 3rd 2nd",
        "34th 3rd 2nd"
    ),
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
        "Words with all consonants like cnn are acronyms",
        "Words With All Consonants Like CNN Are Acronyms"
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
        "Starting a Hyphen Delimited Sub-Phrase With a Small Word - a Trick, Perhaps?",
        "Starting a Hyphen Delimited Sub-Phrase With a Small Word - A Trick, Perhaps?"
    ),
    (
        "Hyphen Delimited Sub-Phrase With a Small Word in Quotes - 'a Trick, Perhaps?'",
        "Hyphen Delimited Sub-Phrase With a Small Word in Quotes - 'A Trick, Perhaps?'"
    ),
    (
        'Hyphen Delimited sub-phrase with a small word in quotes - "a trick, perhaps?"',
        'Hyphen Delimited Sub-Phrase With a Small Word in Quotes - "A Trick, Perhaps?"'
    ),
    (
        "Snakes on a Plane - The TV Edit - The Famous Line",
        "Snakes on a Plane - The TV Edit - The Famous Line"
    ),
    (
        "Starting an Em Dash Delimited Sub-Phrase With a Small Word — a Trick, Perhaps?",
        "Starting an Em Dash Delimited Sub-Phrase With a Small Word — A Trick, Perhaps?"
    ),
    (
        "Em Dash Delimited Sub-Phrase With a Small Word in Quotes — 'a Trick, Perhaps?'",
        "Em Dash Delimited Sub-Phrase With a Small Word in Quotes — 'A Trick, Perhaps?'"
    ),
    (
        'Em Dash Delimited sub-phrase with a small word in quotes — "a trick, perhaps?"',
        'Em Dash Delimited Sub-Phrase With a Small Word in Quotes — "A Trick, Perhaps?"'
    ),
    (
        "Snakes on a Plane — The TV Edit — The Famous Line",
        "Snakes on a Plane — The TV Edit — The Famous Line"
    ),
    (
        "EPISODE 7 — THE FORCE AWAKENS",
        "Episode 7 — The Force Awakens"
    ),
    (
        "episode 7 – The force awakens",
        "Episode 7 – The Force Awakens"
    ),
    (
        "THE CASE OF X ≤ 7",
        "The Case of X ≤ 7"
    ),
    (
        "the case of X ≤ 7",
        "The Case of X ≤ 7"
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
    ),
    (
        "Mr McTavish went to MacDonalds",
        "Mr McTavish Went to MacDonalds"
    ),
    (
        "this shouldn't\nget mangled",
        "This Shouldn't\nGet Mangled"
    ),
    (
        "this is http://foo.com",
        "This Is http://foo.com"
    ),
    (
        "mac mc MAC MC machine",
        "Mac Mc MAC MC Machine",
    ),
    (
        "FOO BAR 5TH ST",
        "Foo Bar 5th St",
    ),
    (
        "foo bar 5th st",
        "Foo Bar 5th St",
    ),
    (
        "l'grange l'grange l'Grange l'Grange",
        "l'Grange l'Grange l'Grange l'Grange",
    ),
    (
        "L'grange L'grange L'Grange L'Grange",
        "l'Grange l'Grange l'Grange l'Grange",
    ),
    (
        "l'GranGe",
        "l'GranGe",
    ),
    (
        "o'grange O'grange o'Grange O'Grange",
        "O'Grange O'Grange O'Grange O'Grange",
    ),
    (
        "o'grange's O'grange's o'Grange's O'Grange's",
        "O'Grange's O'Grange's O'Grange's O'Grange's",
    ),
    (
        "O'GranGe",
        "O'GranGe",
    ),
    (
        "o'melveny/o'doyle o'Melveny/o'doyle O'melveny/o'doyle o'melveny/o'Doyle o'melveny/O'doyle",
        "O'Melveny/O'Doyle O'Melveny/O'Doyle O'Melveny/O'Doyle O'Melveny/O'Doyle O'Melveny/O'Doyle",
    ),
    (
        "oblon, spivak, mcclelland, maier & neustadt",
        "Oblon, Spivak, McClelland, Maier & Neustadt",
    ),
    (
        "Mcoblon, spivak, mcclelland, mcmaier, & mcneustadt",
        "McOblon, Spivak, McClelland, McMaier, & McNeustadt",
    ),
    (
        "mcfoo-bar, MCFOO-BAR, McFoo-bar, McFoo-Bar, mcfoo-mcbar, foo-mcbar",
        "McFoo-Bar, McFoo-Bar, McFoo-Bar, McFoo-Bar, McFoo-McBar, Foo-McBar",
    ),
    (
        "'QUOTE' A GREAT",
        "'Quote' a Great",
    ),
    (
        "‘QUOTE’ A GREAT",
        "‘Quote’ a Great",
    ),
    (
        "“YOUNG AND RESTLESS”",
        "“Young and Restless”",
    ),
    (
        "EL NIÑO A ARRIVÉ HIER",
        "El Niño a Arrivé Hier",
    ),
    (
        "YEA NO",
        "Yea No",
    ),
    (
        "ÝÆ ÑØ",
        "Ýæ Ñø",
    ),
    (
        "yea no",
        "Yea No",
    ),
    (
        "ýæ ñø",
        "Ýæ Ñø",
    ),
)


def test_initials_regex():
    """Test - uppercase initials regex with A.B"""
    from titlecase import UC_INITIALS
    assert bool(UC_INITIALS.match('A.B')) is True


def test_initials_regex_2():
    """Test - uppercase initials regex with A.B."""
    from titlecase import UC_INITIALS
    assert bool(UC_INITIALS.match('A.B.')) is True


def test_initials_regex_3():
    """Test - uppercase initials regex with ABCD"""
    from titlecase import UC_INITIALS
    assert bool(UC_INITIALS.match('ABCD')) is False


def check_input_matches_expected_output(in_, out):
    """Function yielded by test generator"""
    try:
        assert titlecase(in_) == out
    except AssertionError:
        print("{0} != {1}".format(titlecase(in_), out))
        raise


def test_at_and_t():
    def at_n_t(word, **kwargs):
        if word.upper() == "AT&T":
            return word.upper()
    print(titlecase("at&t", callback=at_n_t))
    assert titlecase("at&t", callback=at_n_t) == "AT&T"


def test_input_output():
    """Generated tests"""
    for data in TEST_DATA:
        yield check_input_matches_expected_output, data[0], data[1]


def test_callback():
    def abbreviation(word, **kwargs):
        if word.upper() in ('TCP', 'UDP'):
            return word.upper()
    s = 'a simple tcp and udp wrapper'
    # Note: this library is able to guess that all-consonant words are acronyms, so TCP
    # works naturally, but others will require the custom list
    assert titlecase(s) == 'A Simple TCP and Udp Wrapper'
    assert titlecase(s, callback=abbreviation) == 'A Simple TCP and UDP Wrapper'
    assert titlecase(s.upper(), callback=abbreviation) == 'A Simple TCP and UDP Wrapper'
    assert titlecase(u'crème brûlée', callback=lambda x, **kw: x.upper()) == u'CRÈME BRÛLÉE'


def test_set_small_word_list():
    assert titlecase('playing the game "words with friends"') == 'Playing the Game "Words With Friends"'
    set_small_word_list('a|an|the|with')
    assert titlecase('playing the game "words with friends"') == 'Playing the Game "Words with Friends"'


def test_custom_abbreviations():
    with tempfile.NamedTemporaryFile(mode='w') as f:
        f.write('UDP\nPPPoE\n')
        f.flush()
        # This works without a wordlist, because it begins mixed case
        assert titlecase('sending UDP packets over PPPoE works great') == 'Sending UDP Packets Over PPPoE Works Great'
        # Without a wordlist, this will do the "wrong" thing for the context
        assert titlecase('SENDING UDP PACKETS OVER PPPOE WORKS GREAT') == 'Sending Udp Packets Over Pppoe Works Great'
        # A wordlist can provide custom acronyms
        assert titlecase('sending UDP packets over PPPoE works great', wordlist_file=f.name) == 'Sending UDP Packets Over PPPoE Works Great'


if __name__ == "__main__":
    import nose
    nose.main()
