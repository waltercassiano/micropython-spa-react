import btree
import ulogging as logging

class Mydb:
    db = None
    f = None
    log = logging.getLogger("Mydb - Class")
    def __init__(self):
        self.connect()

    def connect(self):
        try:
            self.f = open("espdb", "r+b")
        except OSError:
            self.f = open("espdb", "w+b")
        self.db = btree.open(self.f)
        self.log.info("Database initiated with success")

    def setItem(self, key, value):
        try:
            self.db[key.encode()] = value.encode()
            self.log.info("Key stored with sucess: key: %s - value: %s", key, value)
        except Exception:
            self.log.error("Database error on save")


    def getItem(self, key):
        try:
            value = self.db[key.encode()]
            self.log.info("Key recovered with sucess: key: %s - value: %s", key, value.decode())
            return value.decode()
        except Exception:
            self.log.error("Database error on get: " + key.encode())

    def close(self):
        self.db.close()
        self.f.close()
        self.log.info("Database closed")
