# -*- coding: utf-8 -*-
"""This module has methods that are used in the other modules in this package."""

import os


def are_flask_environment_variable_set() -> bool:
    """Check if all the Flask environment variables are set.

    Raises
    ------
    KeyError
        If any of the environment variables are not set.

    Returns
    -------
    bool:
        True if all the environment variables are set else False if any is missing.

    """
    try:
        os.environ['FLASK_ENV']  # pylint: disable=W0104
        print('The FLASK_ENV is set')
    except KeyError:
        print('The FLASK_ENV is not set')
        return False

    try:
        os.environ['FLASK_APP']  # pylint: disable=W0104
        print('The FLASK_APP is set')
    except KeyError:
        print('The FLASK_APP is not set')
        return False

    return True
