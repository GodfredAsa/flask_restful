from user import User
from werkzeug.security import safe_str_cmp


# these 2 methods would be used to identify and authenticate users
def authenticate(username, password):
    user = User.find_by_username(username)
    if user and safe_str_cmp(user.password, password):
        return user


def identity(payload):
    use_id = payload['identity']
    return User.find_by_id(use_id)
