# app/models/Example.py

from app.extensions.database import db

class Example(db.Model):
    id = db.Column(db.Integer, primary_key=True)
