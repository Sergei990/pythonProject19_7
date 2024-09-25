# import jwt
# from flask import request, current_app
#
# from flask_restx import abort
#
# from configuration.constante import JWT_SECRET, JWT_ALGO
# from flask import current_app
#
# from main import app
#
from flask import request
from flask_restx import abort

# from main import app


# from main import app


# from main import app


# from main import context, app


# from main import app


# from main import app


# def admin_receiver(func):
#     def wrapper(*args, **kwargs):
#
#         if 'Authorization' not in request.headers:
#             abort(401)
#         data = request.headers['Authorization']
#         token = data.split('Bearer ')[-1]
#         role = None
#         try:
#             user = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGO])
#             role = user.get('role', 'admin')
#         except Exception:
#             abort(401)
#         if role != 'admin':
#             abort(403)
#         return func(*args, **kwargs)
#     return wrapper()
#
def auth_required(func):
    def wrapper(*args, **kwargs):
        # with app.app_context():
        token = request.headers
        if not token:
            abort(401)
        return func(*args,**kwargs)
    return wrapper()

class Authentication:

    # def __init__(self, headers):
    #
    #     self.headers = headers

    def auth_user(self,data):
        if 'Authentication' not in data:
            abort(401)

# with app.test_request_context()