from db.run_sql import run_sql
from models.country import Country



# saves countries
def save(country):
    sql = "INSERT INTO countries (name, continent) VALUES (%s, %s) RETURNING *"
    values = [country.name, country.continent]
    results = run_sql(sql, values)
    id = results[0]['id']
    country.id = id

# selects all countries
def select_all():
    countries = []
    sql = "SELECT * FROM countries"
    results = run_sql(sql)

    for row in results:
        country = Country(row["name"], row["continent"], row["id"])
        countries.append(country)
    return countries

# selects country by id
def select(id):
    country = None
    sql = "SELECT * FROM countries WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        country = Country(result["name"], result["continent"], result["id"])
    return country

# delete all countrys
def delete_all():
    sql = "DELETE  FROM countries"
    run_sql(sql)

# delete country by id
def delete(id):
    sql = "DELETE  FROM countries WHERE id = %s"
    values = [id]
    run_sql(sql, values)


# displays countries by contients
def display_contients():
    continents = []
    sql = "SELECT DISTINCT continent FROM countries ORDER BY continent ASC"
    results = run_sql(sql)
    for row in results:
        continents.append(row["continent"])
    return continents


# displays countries by continent 
def display_country_by_continent(continent):
    countries = []
    sql = "SELECT * FROM countries WHERE continent = %s"
    values = [continent]
    results = run_sql(sql, values)
    for row in results:
        country = Country(row["name"], row["continent"], row["id"])
        countries.append(country)
    return countries




