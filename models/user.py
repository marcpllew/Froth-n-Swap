import bcrypt
import database


def insert_user(name, email, password):
    password_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    database.sql_write("INSERT into users (name, email, password) VALUES (%s, %s, %s);", [name, email, password_hash])

def get_user_by_email(email):
    results = database.sql_select('SELECT * FROM users WHERE email = %s;', [email])
    if len(results) > 0:
        results = results[0]
        return results
    else:
        return None


def get_user_by_id(id):
    results = database.sql_select('SELECT email, name FROM users WHERE email = %s;', [id])
    results = results[0]
    return results


def get_all_users():
    results = database.sql_select('SELECT email, name FROM users', [])
    return results

def update_user(id, name, email):
    pass

def delete_user(id):
    pass