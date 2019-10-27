from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
import logging
from logging.handlers import RotatingFileHandler
import os

piinvernadero = Flask(__name__)
piinvernadero.config.from_object(Config)
db = SQLAlchemy(piinvernadero)
migrate = Migrate(piinvernadero, db)
login = LoginManager(piinvernadero)
login.login_view = 'login'

from piinvernadero import routes, models, errors


if not piinvernadero.debug:
    if piinvernadero.config['MAIL_SERVER']:
        auth = None
        if piinvernadero.config['MAIL_USERNAME'] or piinvernadero.config['MAIL_PASSWORD']:
            auth = (piinvernadero.config['MAIL_USERNAME'], piinvernadero.config['MAIL_PASSWORD'])
        secure = None
        if piinvernadero.config['MAIL_USE_TLS']:
            secure = ()
        mail_handler = SMTPHandler(
            mailhost=(piinvernadero.config['MAIL_SERVER'], piinvernadero.config['MAIL_PORT']),
            fromaddr='no-reply@' + piinvernadero.config['MAIL_SERVER'],
            toaddrs=piinvernadero.config['ADMINS'], subject='Invernalio Failure',
            credentials=auth, secure=secure)
        mail_handler.setLevel(logging.ERROR)
        piinvernadero.logger.addHandler(mail_handler)
    if not os.path.exists('logs'):
        os.mkdir('logs')
    file_handler = RotatingFileHandler('logs/invernalio.log', maxBytes=10240,
                                       backupCount=10)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)

    app.logger.setLevel(logging.INFO)
    app.logger.info('Invernalio startup')