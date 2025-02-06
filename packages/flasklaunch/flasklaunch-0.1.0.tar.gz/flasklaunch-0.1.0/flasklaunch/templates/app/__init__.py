# app/__init__.py
from flasklaunch import Flask
from app.config import configuration

def create_app():
    app = Flask(__name__)
    configuration.init_app(app)
    configuration.load_extensions(app)
    return app