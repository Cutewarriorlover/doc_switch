"""
This file records all currently used SphinxDoc formats (SphinxDoc, EpyDoc,
NumpyDoc, and GoogleDoc).
"""

from enum import Enum


class DocFormat(Enum):
    """
    This enumeration records all currently used SphinxDoc formats (SphinxDoc,
    EpyDoc, NumpyDoc, and GoogleDoc).
    """

    SPHINX_DOC = "sphinx"
    EPY_DOC = "epy"
    NUMPY_DOC = "numpy"
