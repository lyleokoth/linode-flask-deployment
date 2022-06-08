# -*- coding: utf-8 -*-
"""This module sets up the fixtures that will be used in our testing."""

import os
import sys

import pytest

from api import app, db


@pytest.fixture
def client():
    """Create the test client."""
    test_client = app.test_client()
    with app.app_context():
        db.create_all()

        yield test_client  # this is where the testing happens!

        db.drop_all()
