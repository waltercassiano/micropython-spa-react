from .model import Model
class ConfigModel(Model):
    config_db_key = None
    wifi = dict()

    def __init__(self, db):
        self.db = db

    def save(self, schema, key, value):
        super().insert(schema, key, value)