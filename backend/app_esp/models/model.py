import ujson
class Model:
    db = None

    def insert(self, schema, value, serialize=True):
        if serialize is True:
            value = ujson.dumps(value)
        self.db.setItem(schema, value)

    def get(self, schema, unserialize=True):
        if not self.schema_exists(schema):
            return None

        if unserialize is True:
           return ujson.loads(self._get(schema))
        return self._get(schema)

    def _get(self, key):
        return self.db.getItem(key)

    def schema_exists(self, schema):
        return self._get(schema) is not None