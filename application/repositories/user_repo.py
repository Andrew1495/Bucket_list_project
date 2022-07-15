from itertools import count
from db.run_sql import run_sql
from models.user import User


def save(user):
    sql = "INSERT INTO users (name) VALUES  (%s) RETURNING *"
    values = [user.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    user.id = id

def select_all():
    users = []

    sql = "SELECT * FROM users"
    results = run_sql(sql)

    for row in results:
        user= User(row["name"], row["id"])
        users.append(user)
    return users

def select(id):
    user= None
    sql = "SELECT * FROM users WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        user = User(result["name"],result["id"])
    return user

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
    
