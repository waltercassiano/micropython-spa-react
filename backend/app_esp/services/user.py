from ..entity import User
import ulogging as logging

class UserService:
    user_model = None
    log = None
    def __init__(self, user_model):
        self.user_model = user_model
        self.log = logging.getLogger("UserService")

    def user_exists(self, user):
        userDb = self.user_model.getUserById(user_name=user)

        if userDb and userDb.get("name") == user:
            return True

        return False

    def auth_user(self, user_name_to_auth, user_password):
        self.log.info("User to auteticate: %s",  user_name_to_auth)

        if not self.user_exists(user_name_to_auth):
            return False

        user = self.user_model.getUserById(user_name=user_name_to_auth)

        if user and user.get("name") == user_name_to_auth and user.get("pwd") == user_password:
            self.log.info("User autenticate with success: %s", user_name_to_auth)
            return True

        self.log.info("User autenticate error: %s", user_name_to_auth)
        return False

    def add_user(self, user_id, pwd):
        if self.user_exists(user_id):
            return

        user = User()
        user.setEmail("")
        user.setName(user_id)
        user.setPwd(pwd)
        self.user_model.save("users", user_id, user)

