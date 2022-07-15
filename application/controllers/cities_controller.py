from flask import Flask, render_template, Blueprint
import repositories.country_repo as country_repo
import repositories.city_repo as city_repo


from flask import Blueprint

cities_blueprint = Blueprint("cities", __name__)

@cities_blueprint.route("/cities")
def cities():
    cities = city_repo.select_all()
    return render_template("cities/index.html", cities=cities)



