import logging
from logging.handlers import SMTPHandler, RotatingFileHandler
import os
from flask import Flask, request, current_app
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
#from flask_mail import Mail
from flask_bootstrap import Bootstrap
#from flask_moment import Moment
from flask_babel import Babel, lazy_gettext as _l
from config import Config
#from flask import Blueprint

db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()
login.login_view = 'auth.login'
login.login_message = _l('Please log in to access this page.')
#mail = Mail()
bootstrap = Bootstrap()
#moment = Moment()
babel = Babel()



def create_app(config_class=Config):
    piinvernadero = Flask(__name__)
    piinvernadero.config.from_object(config_class)

    db.init_app(piinvernadero)
    migrate.init_app(piinvernadero, db)
    login.init_app(piinvernadero)
    #mail.init_app(piinvernadero)
    bootstrap.init_app(piinvernadero)
    #moment.init_app(piinvernadero)
    babel.init_app(piinvernadero)


    from piinvernadero.errors import bp as errors_bp
    piinvernadero.register_blueprint(errors_bp)

    from piinvernadero.auth import bp as auth_bp
    piinvernadero.register_blueprint(auth_bp, url_prefix='/auth')

    from piinvernadero.role import bp as role_bp
    piinvernadero.register_blueprint(role_bp, url_prefix='/role')

    from piinvernadero.main import bp as main_bp
    piinvernadero.register_blueprint(main_bp)

    if not piinvernadero.debug and not piinvernadero.testing:
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
        piinvernadero.logger.addHandler(file_handler)

        piinvernadero.logger.setLevel(logging.INFO)
        piinvernadero.logger.info('Invernalio startup')
    return piinvernadero

@babel.localeselector
def get_locale():
    #return request.accept_languages.best_match(piinvernadero.config['LANGUAGES'])
    return 'es'

from piinvernadero import models
