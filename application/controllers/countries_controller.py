from flask import Flask, render_template, Blueprint
import repositories.country_repo as country_repo
import repositories.city_repo as city_repo
import repositories.user_repo as user_repo

countries_blueprint = Blueprint("countries", __name__)

# shows all countries
@countries_blueprint.route("/countries")
def countries():
    countries = country_repo.select_all()
    return render_template("countries/index.html", countries=countries)


# shows citys within a country
@countries_blueprint.route("/countries/<id>/cities")
def cities_by_country_id(id):
    user = user_repo.find_logged_in_user()
    cities = city_repo.displaying_cities_by_country(id,user)
    return render_template("cities/index.html", cities=cities)


# shows all continents
@countries_blueprint.route("/continents")
def continents():
    continents = country_repo.display_contients()
    return render_template("countries/continents.html" , continents=continents)

# shows countries by contients
@countries_blueprint.route("/continents/<id>/countries")
def countries_by_continents(id):
    countries = country_repo.display_country_by_continent(id)
    return render_template("countries/index.html", countries=countries)

# shows antarctica
@countries_blueprint.route("/continents/antarctica")
def antarctica():
    return render_template("countries/antarctica.html")