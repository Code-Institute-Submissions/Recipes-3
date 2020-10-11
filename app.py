import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = "recipe_manager"
app.config["MONGO_URL"] = "mongodb+srv://John:Fuck123@cluster0.kkcfz.mongodb.net/recipe_manager?retryWrites=true&w=majority"

mongo = PyMongo(app)

@app.route("/", methods=["GET", "POST", "DELETE"])
@app.route("/get_recipes")
def get_recipes():
    return render_template("recipes.html", recipes=mongo.db.tasks.find())


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT", 5000)),
            debug=True)