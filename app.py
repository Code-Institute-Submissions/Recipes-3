import os
from flask import (Flask, render_template, redirect, request, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
if os.path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("recipe_manager")
app.config["MONGO_URI"] = os.environ.get("mongodb+srv://John:Abc123@cluster0.kkcfz.mongodb.net/recipe_manager?retryWrites=true&w=majority")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)

@app.route("/", methods=["GET", "POST", "DELETE"])
@app.route("/get_recipes")
def get_recipes():
    recipes = mongo.db.recipes.find()
    return render_template("recipes.html", recipes=recipes)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT", 5000)),
            debug=True)