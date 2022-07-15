from flask import Flask, render_template
from repositories import countries_repo

from flask import Blueprint

countries_blueprint = Blueprint("countries", __name__)

@countries_blueprint.route("/countries")
def tasks():
    countries = countries_repo.select_all()
    return render_template("countries/index.html", countries=countries)