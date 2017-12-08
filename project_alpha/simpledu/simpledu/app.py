from flask import Flask
# from simpledu.config import configs
from simpledu.models import db
from simpledu.config import DevelopmentConfig


def register_all_blueprint(app):
    from simpledu.handlers import front, course, admin, user
    app.register_blueprint(front)
    app.register_blueprint(course)
    app.register_blueprint(admin)
    app.register_blueprint(user)


def create_app(config):
    app = Flask(__name__)
    # app.config.from_object(configs.get(config))
    app.config.from_object(DevelopmentConfig)
    db.init_app(app)
    register_all_blueprint(app)
    return app
