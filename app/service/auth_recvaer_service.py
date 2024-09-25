import base64
import datetime
import hashlib
import calendar

import jwt

from configuration.constante import PWD_HASH_SALT, PWD_HASH_ITERATIONS, JWT_SECRET, JWT_ALGO


class AuthReceiverDAO:

    def generation_password(self, password):
        password_hash = hashlib.pbkdf2_hmac('sha512', password.encode('UTF-8'),
                                            PWD_HASH_SALT, PWD_HASH_ITERATIONS)
        return base64.b64encode(password_hash)

    def check_password(self, password_user, password_bd):
        if password_bd != password_user:
            return False
        return True

    def generation_token(self, data):
        min_1 = datetime.datetime.utcnow() + datetime.timedelta(minutes=1)
        data['exp'] = calendar.timegm(min_1.timetuple())
        return jwt.encode(data, JWT_SECRET, algorithm=JWT_ALGO)

    # def
