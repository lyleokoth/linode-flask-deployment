# -*- coding: utf-8 -*-
"""This module sets up the fixtures that will be used in our testing."""

import pytest

from api import create_app


@pytest.fixture
def client():
    """Create the test client."""
    app = create_app()
    test_client = app.test_client()
    return test_client
