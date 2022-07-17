from flask import Flask, redirect, render_template, Blueprint, request
from repositories.city_repo import select
import repositories.user_repo as user_repo
import repositories.want_to_visit_repo as want_to_visit_repo


user_blueprint = Blueprint("user", __name__)


@user_blueprint.route("/user")
def user(id=1):
    user = user_repo.select(id)
    bucket_list = want_to_visit_repo.select_all()
    return render_template("users/index.html", user=user, bucket_list=bucket_list)


@user_blueprint.route("/user/<id>/delete", methods= [ "GET", "POST"])
def delete(id):
    remove = want_to_visit_repo.select(id)
    want_to_visit_repo.delete(remove.id)
    return redirect("/user")
