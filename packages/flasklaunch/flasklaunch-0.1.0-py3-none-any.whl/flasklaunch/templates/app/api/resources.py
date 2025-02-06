# app/api/resources.py

from flasklaunch import jsonify
from flask_restful import Resource

class HomeResource(Resource):
    def get(self):
        return jsonify({"message": "Welcome to the home page!"})

