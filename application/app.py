from flask import Flask, render_template, redirect
from controllers.countries_controller import countries_blueprint
from controllers.cities_controller import cities_blueprint
from controllers.users_controller import user_blueprint
import repositories.user_repo as user_repo


app = Flask(__name__)


app.register_blueprint(countries_blueprint)
app.register_blueprint(cities_blueprint)
app.register_blueprint(user_blueprint)

@app.route('/')
def login():
    user_repo.log_out()
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template("home.html")


if __name__ == '__main__':
    app.run(debug=True)
