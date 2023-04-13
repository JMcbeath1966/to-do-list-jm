from flask import render_template, request, redirect, url_for
from taskmanager import app, db
from taskmanager.models import Category, Task


# These are calling python functions, not the app route
@app.route("/")
def home():  
    return render_template("tasks.html")


@app.route("/categories")
def catergories():
    return render_template("categories.html")


@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    if request.method == "POST":
        category = Category(category_name=request.form.get("category_name"))
        db.session.add(category)
        db.session.commit()
        return redirect(url_for("categories"))
    return render_template("add_category.html")


