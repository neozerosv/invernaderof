from flask import Blueprint

bp = Blueprint('errors', __name__)

from piinvernadero.errors import handlers