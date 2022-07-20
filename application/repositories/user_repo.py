
from db.run_sql import run_sql
from models.user import User

# saves a new user if name is not found
def save(user):
    found = select_user_by_name(user.name)
    if found != False:
        new_user = False
        return new_user
    else:
        sql = "INSERT INTO users (name, password, logged_in) VALUES  (%s,%s, %s) RETURNING *"
        values = [user.name, user.password, user.logged_in]
        results = run_sql(sql, values)
        id = results[0]['id']
        user.id = id

# selects all users
def select_all():
    users = []
    sql = "SELECT * FROM users"
    results = run_sql(sql)

    for row in results:
        user= User(row["name"],row["password"], row["logged_in"], row["id"])
        users.append(user)
    return users


# select user by id
def select(id):
    user= None
    sql = "SELECT * FROM users WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        user = User(result["name"], result["password"],result["logged_in"],result["id"])
    return user


# delete all users
def delete_all():
    sql = "DELETE  FROM users"
    run_sql(sql)

# delete user by id
def delete(id):
    sql = "DELETE  FROM users WHERE id = %s"
    values = [id]
    run_sql(sql, values)

# updates user log in 
def update(user):
    sql = "UPDATE users SET logged_in = %s WHERE id = %s"
    values = [user.logged_in, user.id]
    run_sql(sql, values)




# finds user by name
def select_user_by_name(name):
    sql = "SELECT * FROM users WHERE name = %s"
    values = [name]
    result = run_sql(sql, values)
    if len(result) != 0:
        result = result[0]
        user = User(result["name"], result["password"], result["logged_in"],result["id"])
        return user
    else:
        user = False
        return user

# checks to see if a user is currently logged in
def check_logged_in(user):
    sql = "SELECT * FROM users WHERE name = %s AND logged_in = True"
    values = [user.name]
    result = run_sql(sql, values)
    if len(result) != 0:
        logged_in = True
        return logged_in
    else:
        logged_in = False
        return logged_in
    
# returns the user who is logged in
def find_logged_in_user():
    sql = "SELECT * FROM users WHERE logged_in = True"
    results = run_sql(sql)
    if results:
        result = results[0]
        user = User(result["name"],result["password"], result["logged_in"],result["id"])
    else:
        user = None
    return user
    

# logs out all users
def log_out():
    users = select_all()
    for user in users:
        user.logged_in = False
        update(user)

# checks password matches input password 
def verify_password(user_name, user_password):
    verified = False
    user_check = select_user_by_name(user_name)
    if user_check == False:
        return verified
    elif user_password == user_check.password:
        verified = True
        return verified
    else:
        return verified



