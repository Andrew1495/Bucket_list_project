from flask import Flask, render_template
from repositories import country_repository

from flask import Blueprint

countries_blueprint = Blueprint("countries", __name__)

@countries_blueprint.route('/countries')
def tasks():
    return render_template("countries/index.html",)