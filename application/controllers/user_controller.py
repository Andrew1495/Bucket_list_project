from flask import Flask, redirect, render_template, Blueprint, request
from repositories.city_repo import select
import repositories.user_repo as user_repo
import repositories.want_to_visit_repo as want_to_visit_repo
import repositories.visit_repo as visit_repo


user_blueprint = Blueprint("user", __name__)


@user_blueprint.route("/user")
def user(id=1):
    user = user_repo.select(id)
    bucket_list = want_to_visit_repo.select_all()
    visited = visit_repo.select_all()
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

