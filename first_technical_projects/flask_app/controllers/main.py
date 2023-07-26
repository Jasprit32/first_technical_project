from flask import render_template,redirect,session,request
from flask_app import app
from flask_app.models.user import User
from flask_app.models.employee import Employee
from flask_app.models.location import Location


@app.route("/")
def index():
    return render_template("landing_page.html")

