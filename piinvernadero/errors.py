from flask import render_template
from piinvernadero import piinvernadero, db

@piinvernadero.errorhandler(404)
def not_found_error(error):
    return render_template('/error/404.html'), 404

@piinvernadero.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('error/500.html'), 500