"""Instrument IO specific errors."""


class NimsGeneralError(Exception):
    """General error for the NIMS file reader."""

    pass


class NimsHeaderError(Exception):
    """Error for the NIMS file header parsing."""

    pass
