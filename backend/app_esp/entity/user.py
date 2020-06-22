class User(dict):

    def __init__(self, *args, **kw):
        super(User, self).__init__(*args, **kw)
        self.__dict__ = self

    def get(self, key, d=None):
        return super().get(key, d=d)

    def setName(self, value):
        super().__setitem__("name", value)

    def setPwd(self, value):
         super().__setitem__("pwd", value)

    def setEmail(self, value):
        super().__setitem__("email", value)