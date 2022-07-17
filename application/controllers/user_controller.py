from flask import Flask, render_template, Blueprint, request
import repositories.user_repo as user_repo



user_blueprint = Blueprint("user", __name__)


@user_blueprint.route("/users")
def users():
    users = user_repo.select_all()
    return render_template("users/index.html", users=users)

@user_blueprint.route("/users/<id>")
def user(id):
    user = user_repo.select(id)
    return render_template("users/user.html", user=user)