from itertools import count
from db.run_sql import run_sql
from models.country import Country
from models.user import User
from models.city import City
from models.visit import Vist
import repositories.city_repo as city_repo
import repositories.user_repo as user_repo




def save(visit):
    sql = "INSERT INTO visited (user_id, country_id) VALUES (%s, %s) RETURNING id"
    values = [visit.user.id , visit.city.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    visit.id = id


def select_all():
    visited = []
    sql = "SELECT * FROM visited"
    results = run_sql(sql)
    for result in results:
        city = city_repo.select(result["country_id"])
        user = user_repo.select(result["user_id"])
        visit = Vist(user, city)
        visit.append(visit)
    return visited




def select(id):
    sql = "SELECT * FROM visited WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        city = city_repo.select(result["country_id"])
        user = user_repo.select(result["user_id"])
        visit = Vist(user, city)
    return visit

def delete_all():
    sql = "DELETE FROM visited"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM visited WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(visit):
    sql = "UPDATE visted SET (user_id, city_id) = (%s, %s) WHERE id = %s"
    values = [visit.user.id, visit.city.id, visit.id]
    run_sql(sql, values)
