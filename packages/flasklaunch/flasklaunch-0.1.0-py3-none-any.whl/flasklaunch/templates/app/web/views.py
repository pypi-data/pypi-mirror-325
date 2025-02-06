# app/web/views.py

from flasklaunch import render_template

def index():
    hello = "Hello World!"
    return render_template("index.html", hello=hello)
