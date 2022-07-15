from flask import Flask, render_template, redirect
from controllers.countries_controller import countries_blueprint
from controllers.cities_controller import cities_blueprint
from controllers.user_controller import user_blueprint


app = Flask(__name__)


app.register_blueprint(countries_blueprint)
app.register_blueprint(cities_blueprint)
app.register_blueprint(user_blueprint)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
