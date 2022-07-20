from db.run_sql import run_sql
from models.visit import Vist
import repositories.city_repo as city_repo
import repositories.user_repo as user_repo



# Saves a users id and city id as visited
def save(visit):
    sql = "SELECT * FROM vistited WHERE user_id = %s AND city_id = %s"
    values = [visit.user.id, visit.city.id]
    test = run_sql(sql, values)
    error = True
    if len(test) > 0:
        return error
    else:
        sql = "INSERT INTO vistited (user_id, city_id) VALUES (%s, %s) RETURNING *"
        values = [visit.user.id ,visit.city.id]
        results = run_sql(sql, values)
        id = results[0]['id']
        visit.id = id


# selects all from visited
def select_all():
    visited = []
    sql = "SELECT * FROM vistited"
    results = run_sql(sql)
    for result in results:
        city = city_repo.select(result["city_id"])
        user = user_repo.select(result["user_id"])
        visit = Vist(user, city, result["id"])
        visited.append(visit)
    return visited



# selects visited by id
def select(id):
    sql = "SELECT * FROM vistited WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        city = city_repo.select(result["city_id"])
        user = user_repo.select(result["user_id"])
        visit = Vist(user, city, result["id"])
    return visit


# deletes all visted
def delete_all():
    sql = "DELETE FROM vistited"
    run_sql(sql)

# deletes visted by id
def delete(id):
    sql = "DELETE FROM vistited WHERE id = %s"
    values = [id]
    run_sql(sql, values)

# updates visited 
def update(visit):
    sql = "UPDATE vistited SET (user_id, city_id) = (%s, %s) WHERE id = %s"
    values = [visit.user.id, visit.city.id, visit.id]
    run_sql(sql, values)

# selects all visited by user id
def select_by_user_id():
    visited = []
    sql = "SELECT * FROM vistited WHERE user_id = %s"
    user = user_repo.find_logged_in_user()
    values = [user.id]
    results = run_sql(sql, values)
    for result in results:
        city = city_repo.select(result["city_id"])
        visit = Vist(user, city, result["id"])
        visited.append(visit)
    return visited
