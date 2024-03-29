from itertools import count
from db.run_sql import run_sql
from models.country import Country
from models.user import User
from models.city import City
from models.visit import Vist
import repositories.city_repo as city_repo
import repositories.user_repo as user_repo
from models.want_to_visit import WantToVisit

# saves to  want to visit
def save(want_to_visit):
    sql = "SELECT * FROM want_to_visit WHERE user_id = %s AND city_id = %s"
    values = [want_to_visit.user.id, want_to_visit.city.id]
    test = run_sql(sql, values)
    error = True
    if len(test) > 0:
        return error
    else:
        sql = "INSERT INTO want_to_visit (user_id, city_id) VALUES (%s, %s) RETURNING *"
        values = [want_to_visit.user.id , want_to_visit.city.id]
        results = run_sql(sql, values)
        id = results[0]['id']
        want_to_visit.id = id

# selects all 
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

# select by id
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

# delete all
def delete_all():
    sql = "DELETE FROM want_to_visit"
    run_sql(sql)

# delete by id
def delete(id):
    sql = "DELETE FROM want_to_visit WHERE id = %s"
    values = [id]
    run_sql(sql, values)

# updates entry in want_to_visit
def update(want_to_visit):
    sql = "UPDATE want_to_vist SET (user_id, city_id) = (%s, %s) WHERE id = %s"
    values = [want_to_visit.user.id, want_to_visit.city.id, want_to_visit.id]
    run_sql(sql, values)


# selects want_to_visit by user id
def select_by_user_id():
    want_to_visits = []
    sql = "SELECT * FROM want_to_visit WHERE user_id = %s"
    user = user_repo.find_logged_in_user()
    values = [user.id]
    results = run_sql(sql, values)
    for result in results:
        city = city_repo.select(result["city_id"])
        want = Vist(user, city, result["id"])
        want_to_visits.append(want)
    return want_to_visits

# selects want_to_visit by city id and user id
def select_by_user_id_city_id(city_id):
    want = None
    sql = "SELECT * FROM want_to_visit WHERE user_id = %s AND city_id = %s"
    user = user_repo.find_logged_in_user()
    values = [user.id, city_id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        city = city_repo.select(result["city_id"])
        want = Vist(user, city, result["id"])
    return want