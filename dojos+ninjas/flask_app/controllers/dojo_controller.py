from flask import render_template, redirect, request 

from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja
from flask_app import app

# Show all dojos
@app.route("/")
def index():
    dojos = Dojo.getAll()
    print(dojos)
    return render_template("dojos.html", dojos=dojos)

#Make new dojo form
@app.route('/create', methods=["POST"])
def createDojo():
    Dojo.save(request.form)
    return redirect('/')


#show just one dojo CHANGE VARABLE FROM USER ID
@app.route("/dojo/<int:id>")
def show_one(id):
    return render_template ("single_dojo.html", dojo = Dojo.allNinjas({"id": id}))


# ONLY THING LEFT IS DISPLAY ALL NINJAS ON THE SINGLE DOJO PAGE, go back to DOG COLLAR LECURE


# Thought that adding this into render template would work but it gives an id error
# ninjas = Dojo.allNinjas({"id": id})