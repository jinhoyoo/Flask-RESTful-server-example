from functools import wraps
from flask import request
from flask_restful import Resource, abort
import config
import base64


def basic_authentication():
    # To-Do: Get API key and API secrete from DB.
    api_key_secrete = "Basic " + \
        base64.encodestring(
            config.API_KEY + ":" + config.API_SECRETE
        ).replace('\n', '')
    if api_key_secrete \
            == request.headers.get("Authorization", ""):
        return True
    else:
        print "Fail to auth."
        return False


def authenticate(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not getattr(func, 'authenticated', True):
            return func(*args, **kwargs)

        acct = basic_authentication()  # custom account lookup function

        if acct:
            return func(*args, **kwargs)

        abort(401)
    return wrapper


class AuthResource(Resource):
    method_decorators = [authenticate]
