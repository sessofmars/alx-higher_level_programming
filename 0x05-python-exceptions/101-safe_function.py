#!/usr/bin/python3

from sys import exc_info, stderr


def safe_function(fct, *args):
    """Executes a function safely"""

    try:
        result = fct(*args)
        return result
    except Exception:
        print("Exception: {}".format(exc_info()[1]), file=stderr)
        return None
