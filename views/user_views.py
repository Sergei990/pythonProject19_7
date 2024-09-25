from flask import request
from flask_restx import Namespace, Resource, abort

from app.DAO.error_auth_DAO import NotUsername, NotPassword, NotRole, error_auth
from app.contener import user_schemas, user_service, user_schema, auth_user


users_ns = Namespace('users')


@users_ns.route('/')
class UserView(Resource):
    # @auth_required
    def get(self):
        auth = request.headers
        if 'Authorization' not in auth:

            abort(401)

        return user_schemas.dump(user_service.get_all_user())

    def post(self):
        try:
            new_user = request.json
            error_auth(new_user)
            return user_service.add_user(new_user)
        except NotUsername :
            return "Нет имени"
        except NotPassword:
            return "Нет пароля"
        except NotRole:
            return "Нет пользователя"


@users_ns.route('/<int:uid>')
class UsersViews(Resource):
    def get(self, uid):

        return user_schema.dump(user_service.get_one_user_by_id(uid))

    def put(self, uid):
        result_put = request.json
        result_put['id'] = uid
        return user_service.update_user(result_put)

    def patch(self, uid):
        result_patch = request.json
        result_patch['id'] = uid
        return user_service.patch_user(result_patch)

    def delete(self, uid):
        if 'Authorization' not in request.headers:
            abort(401)
        data = request.headers.get('Authorization')
        token = data.split('Bearer ')[-1]
        r = data.split('Bearer ')
        print(f' hi={r} {token}')
        answer = auth_user.chek_token(token)
        if not answer:
            abort(401)
        elif answer.get('role') != 'admin':
            abort(403)
        return user_service.delete_user(uid)
