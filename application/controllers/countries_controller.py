from flask import Flask, render_template, Blueprint
import repositories.country_repo as country_repo
import repositories.city_repo as city_repo


countries_blueprint = Blueprint("countries", __name__)

@countries_blueprint.route("/countries")
def countries():
    countries = country_repo.select_all()
    return render_template("countries/index.html", countries=countries)

@countries_blueprint.route("/countries/<id>/cities")
def cities_by_country_id(id):
    cities = city_repo.select_city_by_country(id)
    return render_template("cities/index.html", cities=cities)

