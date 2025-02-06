# app/api/__init__.py

from flasklaunch import Blueprint
from flask_restful import Api

from .resources import HomeResource

bp = Blueprint("api", __name__, url_prefix="/api/v1")
api = Api(bp)

def init_app(app):
    api.add_resource(HomeResource, "/")
    app.register_blueprint(bp)