from itertools import count
from db.run_sql import run_sql
from models.country import Country
from models.user import User
from models.city import City
from models.visit import Vist
import repositories.city_repo as city_repo
import repositories.user_repo as user_repo
from models.want_to_visit import WantToVisit


def save(want_to_visit):
    sql = "INSERT INTO want_to_visit (user_id, city_id) VALUES (%s, %s) RETURNING *"
    values = [want_to_visit.user.id , want_to_visit.city.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    want_to_visit.id = id


def select_all():
    want_to_visits = []
    sql = "SELECT * FROM want_to_visit"
    results = run_sql(sql)
    for result in results:
        city = city_repo.select(result["city_id"])
        user = user_repo.select(result["user_id"])
        want_to_visit = WantToVisit(user, city, result["id"])
        want_to_visits.append(want_to_visit)
    return want_to_visits


def select(id):
    sql = "SELECT * FROM want_to_visit WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        city = city_repo.select(result["city_id"])
        user = user_repo.select(result["user_id"])
        want_to_visit = WantToVisit(user, city, result["id"]) 
    return want_to_visit

def delete_all():
    sql = "DELETE FROM want_to_visit"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM want_to_visit WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(want_to_visit):
    sql = "UPDATE want_to_vist SET (user_id, city_id) = (%s, %s) WHERE id = %s"
    values = [want_to_visit.user.id, want_to_visit.city.id, want_to_visit.id]
    run_sql(sql, values)
