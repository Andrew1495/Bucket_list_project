from db.run_sql import run_sql
from models.country import Country
from models.user import User
from models.city import City
import repositories.country_repo as country_repo



def save(city):
    sql = "SELECT * FROM cities WHERE name = %s"
    values = [city.name]
    test = run_sql(sql, values)
    error = True
    if len(test) > 0:
        return error
    else:
        sql = "INSERT INTO cities (name, country_id) VALUES (%s , %s) RETURNING * "
        values = [city.name, city.country.id]
        results = run_sql(sql, values)
        id = results[0]['id']
        city.id = id
        return error


def select_all():
    cities = []
    sql = "SELECT * FROM cities ORDER BY country_id ,name"
    results = run_sql(sql)
    for result in results:
        country = country_repo.select(result["country_id"])
        city = City(result["name"], country, result["id"])
        cities.append(city)
    return cities



def select(id):
    city = None
    sql = "SELECT * FROM cities WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        country = country_repo.select(result["country_id"])
        city = City(result["name"], country, result["id"])
    return city

def delete_all():
    sql = "DELETE FROM cities"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM cities WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(city):
    sql = "SELECT * FROM cities WHERE name = %s"
    values = [city.name]
    test = run_sql(sql, values)
    error = True
    if len(test) > 0:
        return error
    else:
        sql = "UPDATE cities SET (name, country_id) = (%s, %s) WHERE id = %s"
        values = [city.name, city.country.id, city.id]
        run_sql(sql, values)
        return error



    sql = "SELECT * FROM vistited WHERE user_id = %s AND city_id = %s"
    values = [visit.user.id, visit.city.id]
    test = run_sql(sql, values)
    error = True
    if len(test) > 0:
        return error

def select_city_by_country(id):
    cities = []
    sql = "SELECT * FROM cities WHERE country_id = %s" 
    values = [id]
    country = country_repo.select(id)
    results = run_sql(sql, values)
    for result in results:
        city = City(result["name"], country, result["id"])
        cities.append(city)
    return cities


