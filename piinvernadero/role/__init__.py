from flask import Blueprint

bp = Blueprint('role', __name__)

from piinvernadero.role import routes