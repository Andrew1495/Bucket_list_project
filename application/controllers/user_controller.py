from flask import Flask, render_template, Blueprint
import repositories.user_repo as user_repo



user_blueprint = Blueprint("user", __name__)

@user_blueprint.route("/users")
def user():
    users = user_repo.select_all()
    return render_template("user/index.html", users=users)