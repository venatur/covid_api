from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from config import config

mail = Mail()
boot = Bootstrap()
db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    boot.init_app(app)
    db.init_app(app)
    mail.init_app(app)
    #blueprints
    from app.covid import covid
    app.register_blueprint(covid, url_prefix='/covid')

    return app






