import ujson
class Model:
    db = None

    def insert(self, schema, key, value):
        item_to_save = dict()
        if self.schema_exists(schema):
            item_to_save = self.get(schema)

        item_to_save[key] = value
        self.db.setItem(schema, ujson.dumps(item_to_save))

    def get(self, schema):
        if not self.schema_exists(schema):
            return None
        return ujson.loads(self.db.getItem(schema))

    def schema_exists(self, schema):
        return self.db.getItem(schema) is not None


