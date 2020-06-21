from .model import Model

class UserModel(Model):
    def __init__(self, db):
        self.db = db

    def save(self, schema, key, value):
        super().insert(schema, key, value)

    def getUserById(self, user_name=None, schema="users"):
        users = super().get(schema)
        if users and users[user_name]:
            return users[user_name]
        return None

