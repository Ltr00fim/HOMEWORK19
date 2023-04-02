import hashlib
import base64
import hmac
from dao.user import UserDAO
from config import Config


class UserService:
    def __init__(self, dao: UserDAO):
        self.dao = dao

    def get_one(self, pk):
        return self.dao.get_one(pk)

    def get_by_username(self, username):
        return self.dao.get_by_username(username)

    def get_all(self):
        return self.dao.get_all()

    def create(self, data):
        data['password'] = self.get_hash(data['password'])
        return self.dao.create(data)

    def update(self, id):
        self.dao.update(id)
        return self.dao

    def delete(self, rid):
        self.dao.delete(rid)

    def get_hash(self, password):
        hash_digest = hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),
            Config.PWD_HASH_SALT,
            Config.PWD_HASH_ITERATIONS
        )
        return base64.b64encode(hash_digest)

    def compare_password(self, password_hash, other_password):
        decoded_digist = base64.b64decode(password_hash)

        hash_digest = hashlib.pbkdf2_hmac(
            "sha256",
            other_password.encode("utf-8"),
            Config.PWD_HASH_SALT,
            Config.PWD_HASH_ITERATIONS
        )

        return hmac.compare_digest(decoded_digist, hash_digest)
