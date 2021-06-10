#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Original Perl version by: John Gruber http://daringfireball.net/ 10 May 2008
Python version by Stuart Colville http://muffinresearch.co.uk
License: http://www.opensource.org/licenses/mit-license.php
"""

import argparse
import logging
logger = logging.getLogger(__name__)
import os
import string
import sys

try:
    import regex
except ImportError:
    import re as regex

__all__ = ['titlecase']
__version__ = '2.1.0'

SMALL = r'a|an|and|as|at|but|by|en|for|if|in|of|on|or|the|to|v\.?|via|vs\.?'
PUNCT = r"""!"“#$%&'‘()*+,\-–‒—―./:;?@[\\\]_`{|}~"""

SMALL_WORDS = regex.compile(r'^(%s)$' % SMALL, regex.I)
INLINE_PERIOD = regex.compile(r'[\p{Letter}][.][\p{Letter}]', regex.I)
UC_ELSEWHERE = regex.compile(r'[%s]*?[\p{Letter}]+[\p{Uppercase_Letter}]+?' % PUNCT)
CAPFIRST = regex.compile(r"^[%s]*?([\p{Letter}])" % PUNCT)
SMALL_FIRST = regex.compile(r'^([%s]*)(%s)\b' % (PUNCT, SMALL), regex.I)
SMALL_LAST = regex.compile(r'\b(%s)[%s]?$' % (SMALL, PUNCT), regex.I)
SUBPHRASE = regex.compile(r'([:.;?!\-–‒—―][ ])(%s)' % SMALL)
APOS_SECOND = regex.compile(r"^[dol]{1}['‘]{1}[\p{Letter}]+(?:['s]{2})?$", regex.I)
UC_INITIALS = regex.compile(r"^(?:[\p{Uppercase_Letter}]{1}\.{1}|[\p{Uppercase_Letter}]{1}\.{1}[\p{Uppercase_Letter}]{1})+$")
MAC_MC = regex.compile(r"^([Mm]c|MC)(\w.+)")
MR_MRS_MS_DR = regex.compile(r"^((m((rs?)|s))|Dr)$", regex.I)

class Immutable(object):
    pass

class ImmutableString(str, Immutable):
    pass

class ImmutableBytes(bytes, Immutable):
    pass


def _mark_immutable(text):
    if isinstance(text, bytes):
        return ImmutableBytes(text)
    return ImmutableString(text)


def set_small_word_list(small=SMALL):
    global SMALL_WORDS
    global SMALL_FIRST
    global SMALL_LAST
    global SUBPHRASE
    SMALL_WORDS = regex.compile(r'^(%s)$' % small, regex.I)
    SMALL_FIRST = regex.compile(r'^([%s]*)(%s)\b' % (PUNCT, small), regex.I)
    SMALL_LAST = regex.compile(r'\b(%s)[%s]?$' % (small, PUNCT), regex.I)
    SUBPHRASE = regex.compile(r'([:.;?!][ ])(%s)' % small)


def titlecase(text, callback=None, small_first_last=True):
    """
    :param text: Titlecases input text
    :param callback: Callback function that returns the titlecase version of a specific word
    :param small_first_last: Capitalize small words (e.g. 'A') at the beginning; disabled when recursing
    :type text: str
    :type callback: function
    :type small_first_last: bool

    This filter changes all words to Title Caps, and attempts to be clever
    about *un*capitalizing SMALL words like a/an/the in the input.

    The list of "SMALL words" which are not capped comes from
    the New York Times Manual of Style, plus 'vs' and 'v'.

    """
    lines = regex.split('[\r\n]+', text)
    processed = []
    for line in lines:
        all_caps = line.upper() == line
        words = regex.split('[\t ]', line)
        tc_line = []
        for word in words:
            if callback:
                new_word = callback(word, all_caps=all_caps)
                if new_word:
                    # Address #22: If a callback has done something
                    # specific, leave this string alone from now on
                    tc_line.append(_mark_immutable(new_word))
                    continue

            if all_caps:
                if UC_INITIALS.match(word):
                    tc_line.append(word)
                    continue

            if APOS_SECOND.match(word):
                if len(word[0]) == 1 and word[0] not in 'aeiouAEIOU':
                    word = word[0].lower() + word[1] + word[2].upper() + word[3:]
                else:
                    word = word[0].upper() + word[1] + word[2].upper() + word[3:]
                tc_line.append(word)
                continue

            match = MAC_MC.match(word)
            if match:
                tc_line.append("%s%s" % (match.group(1).capitalize(),
                                         titlecase(match.group(2), callback, True)))
                continue

            match = MR_MRS_MS_DR.match(word)
            if match:
                word = word[0].upper() + word[1:]
                tc_line.append(word)
                continue

            if INLINE_PERIOD.search(word) or (not all_caps and UC_ELSEWHERE.match(word)):
                tc_line.append(word)
                continue
            if SMALL_WORDS.match(word):
                tc_line.append(word.lower())
                continue

            if "/" in word and "//" not in word:
                slashed = map(
                    lambda t: titlecase(t,callback,False),
                    word.split('/')
                )
                tc_line.append("/".join(slashed))
                continue

            if '-' in word:
                hyphenated = map(
                    lambda t: titlecase(t, callback, False),
                    word.split('-')
                )
                tc_line.append("-".join(hyphenated))
                continue

            if all_caps:
                word = word.lower()


            # A term with all consonants should be considered an acronym.  But if it's
            # too short (like "St", don't apply this)
            CONSONANTS = ''.join(set(string.ascii_lowercase)
                                 - {'a', 'e', 'i', 'o', 'u', 'y'})
            is_all_consonants = regex.search('\A[' + CONSONANTS + ']+\Z', word,
                                             flags=regex.IGNORECASE)
            if is_all_consonants and len(word) > 2:
                tc_line.append(word.upper())
                continue

            # Just a normal word that needs to be capitalized
            tc_line.append(CAPFIRST.sub(lambda m: m.group(0).upper(), word))

        if small_first_last and tc_line:
            if not isinstance(tc_line[0], Immutable):
                tc_line[0] = SMALL_FIRST.sub(lambda m: '%s%s' % (
                    m.group(1),
                    m.group(2).capitalize()
                ), tc_line[0])

            if not isinstance(tc_line[-1], Immutable):
                tc_line[-1] = SMALL_LAST.sub(
                    lambda m: m.group(0).capitalize(), tc_line[-1]
                )

        result = " ".join(tc_line)

        result = SUBPHRASE.sub(lambda m: '%s%s' % (
            m.group(1),
            m.group(2).capitalize()
        ), result)

        processed.append(result)

    result = "\n".join(processed)
    logger.debug(result)
    return result


def create_wordlist_filter_from_file(file_path):
    '''
    Load a list of abbreviations from the file with the provided path,
    reading one abbreviation from each line, and return a callback to
    be passed to the `titlecase` function for preserving their given
    canonical capitalization during title-casing.
    '''
    if file_path is None:
        logger.debug('No abbreviations file path given')
        return lambda word, **kwargs: None
    file_path_str = str(file_path)
    if not os.path.isfile(file_path_str):
        logger.debug('No abbreviations file found at ' + file_path_str)
        return lambda word, **kwargs: None
    with open(file_path_str) as f:
        logger.debug('Reading abbreviations from file ' + file_path_str)
        abbrevs_gen = (line.strip() for line in f.read().splitlines() if line)
        abbrevs = {abbr.upper(): abbr for abbr in abbrevs_gen}
        if logger.isEnabledFor(logging.DEBUG):
            for abbr in abbrevs.values():
                logger.debug('Registered abbreviation: ' + abbr)
        return lambda word, **kwargs: abbrevs.get(word.upper())


def cmd():
    '''Handler for command line invocation'''

    # Try to handle any reasonable thing thrown at this.
    # Consume '-f' and '-o' as input/output, allow '-' for stdin/stdout
    # and treat any subsequent arguments as a space separated string to
    # be titlecased (so it still works if people forget quotes)
    parser = argparse.ArgumentParser()
    in_group = parser.add_mutually_exclusive_group()
    in_group.add_argument('string', nargs='*', default=[],
            help='String to titlecase')
    in_group.add_argument('-f', '--input-file',
            help='File to read from to titlecase')
    parser.add_argument('-o', '--output-file',
            help='File to write titlecased output to')
    parser.add_argument('-w', '--wordlist',
            help='Wordlist for acronyms')

    args = parser.parse_args()

    if args.input_file is not None:
        if args.input_file == '-':
            ifile = sys.stdin
        else:
            ifile = open(args.input_file)
    else:
        ifile = sys.stdin

    if args.output_file is not None:
        if args.output_file == '-':
            ofile = sys.stdout
        else:
            ofile = open(args.output_file, 'w')
    else:
        ofile = sys.stdout

    if len(args.string) > 0:
        in_string = ' '.join(args.string)
    else:
        with ifile:
            in_string = ifile.read()

    if args.wordlist is not None:
        wordlist_file = args.wordlist
    else:
        wordlist_file = os.path.join(os.path.expanduser('~'), '.titlecase.txt')
    wordlist_filter = create_wordlist_filter_from_file(wordlist_file)

    with ofile:
        ofile.write(titlecase(in_string, callback=wordlist_filter))
