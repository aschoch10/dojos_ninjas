from flask import render_template, redirect, request 

from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

from flask_app import app

# Route for the render
@app.route("/ninjas/new")
def new_ninja():
    return render_template("ninjas.html", dojos = Dojo.getAll())


# Route for the form
@app.route("/ninjas/create", methods = ['POST'])
def create_ninja():
    Ninja.newNinja(request.form)
    return redirect ('/')