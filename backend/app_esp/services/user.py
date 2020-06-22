from ..entity import User
class UserService:
    user_model = None

    def __init__(self, user_model):
        self.user_model = user_model

    def auth_user(self, user_name_to_auth, user_password):
        user = self.user_model.getUserById(user_name=user_name_to_auth)
        if user and user.get("name") == user_name_to_auth and user.get("pwd") == user_password:
            return True
        return False


    def add_user(self, user_id, pwd):
        user = User()
        user.setEmail("")
        user.setName(user_id)
        user.setPwd(pwd)
        self.user_model.save("users", user_id, user)

