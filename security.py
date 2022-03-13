from user import User
from werkzeug.security import safe_str_cmp

users = [
    User(1, 'bob', 'abcd')
]

# set comprehension
username_mapping = {u.username: u for u in users}
userid_mapping = {u.id: u for u in users}

print(list(username_mapping))
print(list(userid_mapping))


# these 2 methods would be used to identify and authenticate users
def authenticate(username, password):
    user = username_mapping.get(username, None)
    if user and safe_str_cmp(user.password, password):
        return user


def identity(payload):
    use_id = payload['identity']
    return userid_mapping.get(use_id, None)
