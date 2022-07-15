from flask import Flask, render_template, Blueprint
import repositories.country_repo as country_repo


countries_blueprint = Blueprint("countries", __name__)

@countries_blueprint.route("/countries")
def countries():
    countries = country_repo.select_all()
    return render_template("countries/index.html", countries=countries)