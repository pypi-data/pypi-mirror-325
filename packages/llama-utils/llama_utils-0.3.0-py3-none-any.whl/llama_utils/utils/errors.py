"""Errors module."""


class StorageNotFoundError(Exception):
    """ReadOnlyError."""

    def __init__(self, error_message: str):
        """__init__."""
