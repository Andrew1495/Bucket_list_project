from flask import Flask, redirect, render_template, Blueprint, request
from models.user import User
from repositories.city_repo import select
import repositories.user_repo as user_repo
import repositories.want_to_visit_repo as want_to_visit_repo
import repositories.visit_repo as visit_repo


user_blueprint = Blueprint("user", __name__)


@user_blueprint.route("/user")
def user():
    user = user_repo.find_logged_in_user()
    bucket_list = want_to_visit_repo.select_by_user_id()
    visited = visit_repo.select_by_user_id()
    return render_template("users/index.html", user=user, bucket_list=bucket_list, visited=visited)


@user_blueprint.route("/user/<id>/delete_bucket", methods= [ "GET", "POST"])
def delete_bucket(id):
    remove = want_to_visit_repo.select(id)
    want_to_visit_repo.delete(remove.id)
    return redirect("/user")


@user_blueprint.route("/user/<id>/delete_visit", methods= [ "GET", "POST"])
def delete_visit(id):
    remove = visit_repo.select(id)
    visit_repo.delete(remove.id)
    return redirect("/user")

@user_blueprint.route("/login" , methods=["GET" , "POST"])
def login():
    user_name = request.form["user.name"]
    user = user_repo.select_user_by_name(user_name)
    if user == False:
        return render_template("error.html")
    else:
        logged = user_repo.check_logged_in(user)

        if logged == False:
            user.logged_in = True
            user_repo.update(user)
            return redirect("/home")
        else:
            return render_template("error.html")


@user_blueprint.route("/logout")
def log_out():
    user_repo.log_out()
    return redirect("/")

@user_blueprint.route("/register")
def register():
    return render_template("users/register.html")


@user_blueprint.route("/register/new",  methods=["GET" , "POST"])
def new_user():
    user_name = request.form["user.name"]
    user = User(user_name, False)
    complete = user_repo.save(user)
    if complete != False:
        return redirect("/")
    else:
        return render_template("error.html")


