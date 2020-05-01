from .model import Model
import ujson

class ConfigModel(Model):
    config_db_key = None
    wifi = dict()

    def __init__(self, db):
        self.db = db

    def save(self, schema, key, value):
        item_to_save = dict()
        if self.schema_exists(schema):
            item_to_save = self.get(schema)

        item_to_save[key] = value
        self.insert(schema, item_to_save)

    #     wifi_from_db = dict()
    #     print("teste ==========================================")
    #     if self.get_all_wifi() is None:
    #         self.wifi[ssid] = pwd
    #         self._save_all_wifi(ujson.dumps(self.wifi))
    #         return

    #     wifi_from_db = self.get_all_wifi()
    #     wifi_from_db[ssid] = pwd

    #     self._save_all_wifi(wifi_from_db)

    # def delete_wifi(self, ssid):
    #     wifi_from_db = self.get_all_wifi()
    #     wifi_from_db.remove(ssid)
    #     self._save_all_wifi(wifi_from_db)
