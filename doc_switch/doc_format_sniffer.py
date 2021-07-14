"""
This module is the Documentation Sniffer.

It serves the purpose of getting a docstring and trying to figure out which
format it is written in (SphinxDoc, EpyDoc, NumpyDoc, or GoogleDoc). It is
implemented by a series of regular expressions which are then grouped by
documentation type, and tested on the docstring. If none match or there is more
than one type of possible match, then it asks the user to choose.
"""

import re

from doc_switch.doc_formats import DocFormat

_type_regex = {
    "sphinx": [r":(\w+\s?)+:"],
    "epy": [r"@(\w+\s?)+:"],
    "numpy": [r"\w+\s*-+", r"\w+\s*:\s*\w*"]
}


def sniff_type(docstring: str):
    """
    This function tries to figure out which format the docstring is written in.

    Args:
        docstring: The docstring to test against.

    Returns:
        DocFormat: The format of the docstring.
    """

    matches = []
    for sphinx_regex in _type_regex["sphinx"]:
        if re.search(sphinx_regex, docstring):
            matches.append(DocFormat.SPHINX_DOC)

    for epy_regex in _type_regex["epy"]:
        if re.search(epy_regex, docstring):
            matches.append(DocFormat.EPY_DOC)

    for numpy_regex in _type_regex["numpy"]:
        if re.search(numpy_regex, docstring):
            matches.append(DocFormat.NUMPY_DOC)

    if len(set(matches)) > 1:
        answer = input("ERROR: Which?\n" + docstring + "\n\n")
        return answer
    return matches[0]
