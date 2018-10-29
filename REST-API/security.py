# Importing necessary modules
from werkzeug.security import safe_str_cmp
from user import User

#creating users list using User class
users = [
    User(1, 'admin', 'admin')
]

#creating username table
username_dict = {u.username: u for u in users}

#creating userid table
userid_dict = {u.id: u for u in users}

#Authenticating username and password
def authenticate(username, password):
    user = username_dict.get(username, None)
    if user and safe_str_cmp(user.password, password):
        return user

def identity(payload):
    user_id = payload['identity']
    return userid_dict.get(user_id, None)
