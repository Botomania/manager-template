"""
List of known errors, easier to manage
"""

import sys


class errors:
    """
    List of errors
    """

    MANAGER_IMPORT_ERROR = "Couldn't import manager"


def panic(error, exit_code=1):
    """
    Prints the error message and quits
    """
    print(error)
    sys.exit(exit_code)
