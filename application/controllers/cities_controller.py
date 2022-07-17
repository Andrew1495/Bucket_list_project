from flask import Flask, redirect, render_template, Blueprint, request
from controllers.countries_controller import countries
from models.city import City
from models.want_to_visit import WantToVisit
import repositories.country_repo as country_repo
import repositories.city_repo as city_repo
import repositories.want_to_visit_repo as want_to_visit_repo
import repositories.user_repo as user_repo

from flask import Blueprint

cities_blueprint = Blueprint("cities", __name__)
# show all citys
@cities_blueprint.route("/cities")
def cities():
    cities = city_repo.select_all()
    return render_template("cities/index.html", cities=cities)

# show single city
@cities_blueprint.route("/cities/<id>")
def city(id):
    city = city_repo.select(id)
    return render_template("/cities/city.html", city=city)

# edit single city
@cities_blueprint.route("/cities/<id>/edit")
def edit(id):
    city = city_repo.select(id)
    countries= country_repo.select_all()
    return render_template("cities/edit.html", city=city, countries=countries)


# update city
@cities_blueprint.route("/cities/<id>", methods=["POST"])
def update(id):
    country_id = request.form["country_id"]
    city_name = request.form["city.name"]
    country = country_repo.select(country_id)
    city = City(city_name, country, id)
    city_repo.update(city)
    return redirect(f"/cities/{id}")


@cities_blueprint.route("/cities/new")
def new():
    countries = country_repo.select_all()
    return render_template("cities/new.html", countries=countries)

@cities_blueprint.route("/cities", methods = ["POST"])
def create():
    country_id = request.form["country_id"]
    city_name = request.form["city.name"]
    country = country_repo.select(country_id)
    city = City(city_name, country, id)
    city_repo.save(city)
    return redirect("/cities")

@cities_blueprint.route("/bucket_list/<id>", methods=["GET", "POST"])
def add_city_to_bucket_list(id,user_id = 1):
    city = city_repo.select(id)
    user = user_repo.select(user_id)
    want_to_visit = WantToVisit(user, city)
    want_to_visit_repo.save(want_to_visit)
    return redirect("/cities")