from flask import Blueprint

bp = Blueprint('auth', __name__)

from piinvernadero.auth import routes