from mongoengine import *


class User(Document):
    login = StringField(max_length=30, required=True, min_length=6, unique=True)
    password = StringField(max_length=30, required=True, min_length=6)
    isBanned = BooleanField(required=True)
    isAdmin = BooleanField(required=True)


def add_new_user(login, password, is_banned = False, is_admin = False):
    user = User()
    if (len(login) >= 6) and (len(login) <= 30):
        user.login = login
    else:
        return -1

    if (len(password) >= 9) and (len(password) <= 30):
        user.password = password
    else:
        return -1

    user.isBanned = is_banned
    user.isAdmin = is_admin

    user.save()
    return 0


def update_user(login, password, is_banned=False, is_admin=False):
    user = User.objects(login=login)[0]
    if user is None:
        return -1
    if (len(password) >= 9) and (len(password) <= 30):
        user.update(**{"set__password": password})
    else:
        return -1

    if is_banned is not None:
        user.update(**{"set__isBanned": is_banned})
    if is_admin is not None:
        user.update(**{"set__isAdmin": is_admin})
    return 0


def delete_user(login):
    user = User.objects(login=login)
    if user is None:
        return -1
    else:
        user.delete()
        return 0


def get_user(login):
    user = User.objects(login=login)[0]
    if user is None:
        return -1
    else:
        return user


def get_all_users():
    return User.objects()
