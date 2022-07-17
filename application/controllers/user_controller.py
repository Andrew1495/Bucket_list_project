from flask import Flask, render_template, Blueprint, request
import repositories.user_repo as user_repo



user_blueprint = Blueprint("user", __name__)


def load_user(login):
    



@user_blueprint.route("/users")
def user():
    users = user_repo.select_all()
    return render_template("user/index.html", users=users)