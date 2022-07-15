from itertools import count
from db.run_sql import run_sql
from models.country import Country
from models.user import User
from models.city import City

def save(country):
    sql = "INSERT INTO countries (name, continent) VALUES (%s, %s) RETURNING *"
    values = [country.name, country.continent]
    results = run_sql(sql, values)
    id = results[0]['id']
    country.id = id

def select_all():
    countries = []

    sql = "SELECT * FROM countries"
    results = run_sql(sql)

    for row in results:
        breakpoint
        country = Country(row["name"], row["continent"], row["id"])
        countries.append(country)
    return countries

def select(id):
    country = None
    sql = "SELECT * FROM countries WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        country = Country(result["name"], result["continent"], result["id"])
    return country

def delete_all():
    sql = "DELETE  FROM countries"
    run_sql(sql)


def delete(id):
    sql = "DELETE  FROM countries WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(country):
    sql = "UPDATE tasks SET (description, user_id, duration, completed) = (%s, %s) WHERE id = %s"
    values = [country["name"], country["continent"], country["id"]]
    run_sql(sql, values)
    
