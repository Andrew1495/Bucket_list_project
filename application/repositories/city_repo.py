from http.client import FOUND
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
        sql = "INSERT INTO cities (name, country_id, attraction_1, attraction_2, attraction_3) VALUES (%s , %s, %s, %s, %s) RETURNING * "
        values = [city.name, city.country.id,city.attraction_1, city.attraction_2, city.attraction_3]
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
        city = City(result["name"], country,result["attraction_1"], result["attraction_2"], result["attraction_3"],result["id"])
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
        city = City(result["name"], country,result["attraction_1"], result["attraction_2"], result["attraction_3"], result["id"])
    return city

def delete_all():
    sql = "DELETE FROM cities"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM cities WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(city):
        sql = "UPDATE cities SET (name, country_id,attraction_1, attraction_2, attraction_3 ) = (%s, %s, %s, %s, %s) WHERE id = %s"
        values = [city.name, city.country.id, city.attraction_1, city.attraction_2, city.attraction_3, city.id]
        run_sql(sql, values)


def select_city_by_country(id):
    cities = []
    sql = "SELECT * FROM cities WHERE country_id = %s" 
    values = [id]
    country = country_repo.select(id)
    results = run_sql(sql, values)
    for result in results:
        city = City(result["name"], country, result["attraction_1"], result["attraction_2"], result["attraction_3"],result["id"])
        cities.append(city)
    return cities




def check_bucket_visited(id , city):
        sql_1 = "SELECT * FROM vistited WHERE user_id = %s AND city_id = %s"
        values_1 = [id, city.id]
        test_visit = run_sql(sql_1, values_1)
        sql_2 = "SELECT * FROM want_to_visit WHERE user_id = %s AND city_id = %s"
        values_2 = [id, city.id]
        test_bucket = run_sql(sql_2, values_2)
        found = True
        if len(test_visit) > 0 or len(test_bucket) > 0:
            return found
        else:
            found = False
            return found

def displaying_cities(id=1):
    display_cities = []
    cities = select_all()
    for city in cities:
        found = check_bucket_visited(id,city)
        if found == False:
            display_cities.append(city)
    return display_cities

