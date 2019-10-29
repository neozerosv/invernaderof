from flask import Blueprint

bp = Blueprint('main', __name__)

from piinvernadero.main import routes