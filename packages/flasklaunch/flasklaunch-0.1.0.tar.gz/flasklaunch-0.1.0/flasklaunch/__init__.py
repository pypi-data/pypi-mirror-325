# flasklaunch/flasklaunch/__init__.py

from flasklaunch import Flask

def create_app():
    app = Flask(__name__)
    init_app(app)
    return app