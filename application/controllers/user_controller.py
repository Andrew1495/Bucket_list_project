from flask import Flask, redirect, render_template, Blueprint, request
from models.user import User
from repositories.city_repo import select
import repositories.user_repo as user_repo
import repositories.want_to_visit_repo as want_to_visit_repo
import repositories.visit_repo as visit_repo


user_blueprint = Blueprint("user", __name__)

# displays profile
@user_blueprint.route("/user")
def user():
    user = user_repo.find_logged_in_user()
    bucket_list = want_to_visit_repo.select_by_user_id()
    visited = visit_repo.select_by_user_id()
    return render_template("users/index.html", user=user, bucket_list=bucket_list, visited=visited)

# deletes item from bucket List
@user_blueprint.route("/user/<id>/delete_bucket", methods= [ "GET", "POST"])
def delete_bucket(id):
    remove = want_to_visit_repo.select(id)
    want_to_visit_repo.delete(remove.id)
    return redirect("/user")

# deletes item from visit list
@user_blueprint.route("/user/<id>/delete_visit", methods= [ "GET", "POST"])
def delete_visit(id):
    remove = visit_repo.select(id)
    visit_repo.delete(remove.id)
    return redirect("/user")

# logs user in
@user_blueprint.route("/login" , methods=["GET" , "POST"])
def login():
    user_name = request.form["user.name"]
    user_password = request.form["user.password"]
    user = user_repo.select_user_by_name(user_name)
    password_check = user_repo.verify_password(user_name,user_password)

    if user == False or password_check == False:
        return render_template("error.html")
    else:
        logged = user_repo.check_logged_in(user)

        if logged == False:
            user.logged_in = True
            user_repo.update(user)
            return redirect("/home")
        else:
            return render_template("error.html")

# logs out
@user_blueprint.route("/logout")
def log_out():
    user_repo.log_out()
    return redirect("/")

# brings page to register new user
@user_blueprint.route("/register")
def register():
    return render_template("users/register.html")

# takes form info and creates new user
@user_blueprint.route("/register/new",  methods=["GET" , "POST"])
def new_user():
    user_name = request.form["user.name"]
    user_password= request.form["user.password"]
    user = User(user_name,user_password, False)
    complete = user_repo.save(user)
    if complete != False:
        return redirect("/")
    else:
        return render_template("error.html")


