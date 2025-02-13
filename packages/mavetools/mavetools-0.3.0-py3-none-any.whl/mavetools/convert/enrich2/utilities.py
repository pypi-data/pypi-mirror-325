import re
from collections import OrderedDict

import numpy as np
import pandas as pd
from mavehgvs import Variant
from mavehgvs.patterns import dna, protein

from . import constants, exceptions


def is_null(value):
    """
    Checks if the value of the passed string is null, undefined, none, na, n/a, nan or empty.

    Parameters
    __________
    value : Any
        To be checked if is null, undefined, none, na, n/a, nan or empty.

    Returns
    _______
    bool
        `True` if `value` is null, undefined, none, na, n/a, nan or empty.
    """
    value = str(value).strip().lower()
    return (not value) or constants.null_value_re.fullmatch(value) is not None


def format_column(values, astype=float):
    """
    Formats a list of values by replacing null float/int values with
    `np.NaN` or null object values with None. All other values
    are typecast to `astype`.

    Parameters
    ----------
    values : list[Union[float, int]]
        List of values to format.
    astype : callable, optional
        Type-casting callback accepting a single argument.

    Returns
    -------
    list[Any]
        List of values with type returned by `astype` and null values
        replaced with `np.NaN`.
    """
    cast_to_numeric = is_numeric(astype)
    none_type = np.NaN if cast_to_numeric else None
    return [none_type if is_null(v) else astype(v) for v in values]


def is_numeric(dtype):
    """
    Returns `True` if a dtype is a subtype of a `float` or `int`.

    Parameters
    ----------
    dtype: type
        Type to check

    Returns
    -------
    bool
    """
    return np.issubdtype(dtype, np.floating) or np.issubdtype(dtype, np.signedinteger)


class NucleotideSubstitutionEvent(object):
    """
    Parses a nucleotide HGVS_ string into a python class. Can only accept
    basic strings of the format `<prefix>.<position><ref>><alt>`

    Attributes
    ----------
    position : int
        Position of the substitution event.
    ref : str, optional.
        The reference base. May be `None` if the substitution is silent.
    alt : str, optional.
        The mutant base. May be `None` if the substitution is silent.
    silent : bool
        `True` if `ref == alt` or the event has the form `<prefix>.<position>=`
    prefix : str
        Prefix of the variant.
    """

    def __init__(self, variant):
        """

        Parameters
        ----------
        variant
        """
        self.variant = variant.strip()
        if self.variant.startswith("p"):
            raise exceptions.InvalidVariantType(
                "'{}' is not a valid DNA/RNA " "substitution event.".format(self.variant)
            )
        var = Variant(self.variant)
        if var.variant_type != "sub" and var.sequence != "=":
            raise exceptions.InvalidVariantType(
                "'{}' is not a valid DNA/RNA " "substitution event.".format(self.variant)
            )
        self.position = int(str(var.positions))
        if var.sequence == "=":
            self.silent = True
            self.ref = None
            self.alt = None
        else:
            self.silent = False
            self.ref = var.sequence[0]
            self.alt = var.sequence[1]
        self.prefix = var.prefix

    def __repr__(self):
        return self.format

    @property
    def format(self):
        """

        Returns
        -------

        """
        print(type("{}.{}".format(self.prefix, self.event)))
        return "{}.{}".format(self.prefix, self.event)

    @property
    def event(self):
        """

        Returns
        -------

        """
        if self.silent:
            return "{pos}=".format(pos=self.position)
        return "{pos}{ref}>{alt}".format(ref=self.ref, pos=self.position, alt=self.alt)

    def codon_position(self, one_based=True):
        """
        Returns the 1-based codon position of a variant.

        Parameters
        ----------
        one_based : bool
            Set as `True` if the variant position expressed in
            1-based coordinates.

        Returns
        -------
        int
            The 1-based codon position of a variant.

        Raises
        ______
        ValueError
            If self.position is less than 0.
        """
        if self.position < 0:
            raise ValueError("Cannot infer codon from negative position.")
        return (self.position - int(one_based)) // 3 + 1

    def codon_frame_position(self, one_based=True):
        """
        Returns the 1-based position of this variant within it's codon.

        Parameters
        ----------
        one_based : bool
            Set as `True` if the variant position expressed in
            1-based coordinates.

        Returns
        -------
        int
            The 1-based position of this variant within it's codon.

        Raises
        ______
        ValueError
            If self.position is less than 0.
        """
        if self.position < 0:
            raise ValueError("Cannot infer codon frame from negative position.")
        return self.position - 3 * (self.codon_position(one_based) - 1) + int(not one_based)


class ProteinSubstitutionEvent(object):
    """
    Parses a protein HGVS_ string into a python class. Can only accept
    basic strings of the format `p.<ref><position><alt>`

    Attributes
    ----------
    position : int
        Position of the substitution event.
    ref : str, optional.
        The reference amino acid in three-letter-code format.
    alt : str, optional.
        The mutant amino acid in three-letter-code format.
    silent : bool
        `True` if `ref == alt` or the event has the form
        `<prefix>.<ref><position>=`.
    prefix : str
        Prefix of the variant.
    """

    def __init__(self, variant):
        """

        Parameters
        ----------
        variant
        """
        self.variant = variant.strip()
        if not self.variant.startswith("p"):
            raise exceptions.InvalidVariantType(
                "'{}' is not a valid DNA/RNA " "substitution event.".format(self.variant)
            )
        var = Variant(self.variant)
        if var.variant_type != "sub" and var.sequence != "=":
            raise exceptions.InvalidVariantType(
                "'{}' is not a valid amino acid " "substitution event.".format(self.variant)
            )
        self._position = None
        self.position = int("".join([n for n in str(var.positions) if n in "0123456789"]))

        if var.sequence == "=":
            self.silent = True
            self.ref = "".join([n for n in str(var.positions) if n not in "0123456789"])
            self.alt = self.ref
        else:
            self.silent = False
            self.ref = var.sequence[0]
            self.alt = var.sequence[1]
        self.prefix = var.prefix

    def __repr__(self):
        """

        Returns
        -------

        """
        return self.format

    @property
    def position(self):
        """

        Returns
        -------

        """
        return self._position

    @position.setter
    def position(self, value):
        """

        Parameters
        ----------
        value

        Returns
        -------

        """
        if value < 1:
            raise ValueError("Protein position cannot be less " "Attempted to set {} in {}".format(value, self.variant))
        self._position = value

    @property
    def format(self):
        """

        Returns
        -------

        """
        return "{}.{}".format(self.prefix, self.event)

    @property
    def event(self):
        """

        Returns
        -------

        """
        if self.silent:
            return "{ref}{pos}=".format(ref=self.ref, pos=self.position)
        return "{ref}{pos}{alt}".format(ref=self.ref, pos=self.position, alt=self.alt)


def split_variant(variant):
    """
    Splits a multi-variant `HGVS` string into a list of single variants. If
    a single variant string is provided, it is returned as a singular `list`.

    Parameters
    ----------
    variant : str
        A valid single or multi-variant `HGVS` string.

    Returns
    -------
    list[str]
        A list of single `HGVS` strings.
    """
    prefix = variant[0]
    if len(variant.split(";")) > 1:
        return ["{}.{}".format(prefix, e.strip()) for e in variant[3:-1].split(";")]
    return [variant]


def format_variant(variant):
    """
    Return None for null variant and strips trailing whitespaces.

    Parameters
    ----------
    variant : str, optional.
        HGVS_ formatted string.

    Returns
    -------
    str
    """
    if variant is None:
        return variant
    return variant.strip()


def hgvs_pro_from_event_list(events):
    """
    Convert a list of protein variant events into a single HGVS string. Removes
    duplicates from `events`.

    Parameters
    __________
    events


    Returns
    _______
    mave_hgvs

    """
    events = list(OrderedDict.fromkeys([format_variant(e) for e in events]).keys())
    if len(events) == 1:
        mave_hgvs = "p.{}".format(format_variant(events[0]))
    else:
        mave_hgvs = "p.[{}]".format(";".join(events))

    match = re.fullmatch(protein.pro_single_variant, mave_hgvs) or re.fullmatch(protein.pro_multi_variant, mave_hgvs)
    if not match:
        raise exceptions.HGVSMatchError("Could not validate parsed variant '{variant}'.".format(variant=mave_hgvs))
    return mave_hgvs


def hgvs_nt_from_event_list(events, prefix):
    """
    Convert a list of variant events into a single HGVS string.

    Parameters
    __________
    events : list[str]
        List of strings of variant events.
    prefix : str
        Prefix of event (i.e., c, r, etc.).

    Returns
    _______
    mave_hgvs : str
        Mave HGVS formatted string.

    Raises
    ______
    HGVSMatchError
        If string is not in Mave HGVS format.
    """
    # remove duplicates
    events = sorted(set(events), key=events.index)

    if len(events) == 1:
        mave_hgvs = "{}.{}".format(prefix, format_variant(events[0]))
    else:
        mave_hgvs = "{}.[{}]".format(prefix, ";".join(format_variant(e) for e in events))

    match = re.fullmatch(dna.dna_single_variant, mave_hgvs) or re.fullmatch(dna.dna_multi_variant, mave_hgvs)

    if not match:
        raise exceptions.HGVSMatchError("Could not validate parsed variant '{hgvs}'.".format(hgvs=mave_hgvs))

    return mave_hgvs


def non_hgvs_columns(columns):
    """
    Takes an iterable of column names and returns a pandas Index object
    containing all entries that are not equal to the HGVS column names.
    The order of the elements is preserved.

    Parameters
    __________
    columns :
        column names

    Returns
    _______
    pandas.core.indexes.base.Index
        All entries not equal to the HGVS column names.
    """
    data_columns = [x for x in columns if x != constants.nt_variant_col and x != constants.pro_variant_col]
    return pd.Index(data_columns)


def hgvs_columns(columns):
    """
    Takes an iterable of column names and returns a pandas Index object
    containing all entries that are equal to the HGVS column names.
    The order of the elements is preserved.

    Parameters
    __________
    columns :
        column names

    Returns
    _______
    pandas.core.indexes.base.Index
        All entries equal to the HGVS column names.
    """
    data_columns = [x for x in columns if x == constants.nt_variant_col or x == constants.pro_variant_col]
    return pd.Index(data_columns)
