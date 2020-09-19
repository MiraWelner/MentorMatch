# really need to figure out why it's called this
# The purpose of this file is to allow users to add and alter information?

from my_app import app
from flask import render_template, request, redirect
import requests

string_char = "Claire"
facts = {"Birthday": "June 4th, 2000", "Favorite Color": "Blue", "Interests": "I like guitar, clarinet, fire-spinning, aerial silks, and trees :)"}
posts = [{"title": "this is my title", "description": "this is my description"}]
@app.route("/")
def index():
    #create objects(?) that html can access
    return render_template("index.html", string_char = string_char)

@app.route("/func_name")
def function_name():
    return redirect("/")

#going to want a create a card function - unless mira is handling this
#unsure if search options take place here or html
