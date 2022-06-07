# -*- coding: utf-8 -*-
"""This module contains the routes associated with the default Blueprint."""
from flask import Blueprint, jsonify

from .models import User

default = Blueprint('default', __name__, template_folder='templates', static_folder='static')


@default.route('/')
def default_route():
    """Confirm that the application is working."""
    return jsonify({'hello': 'from template api'}), 200


@default.route('/users')
def all_users():
    """Get all the users."""
    users = User.query.all()
    return jsonify(users)
