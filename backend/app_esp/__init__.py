from .models import *
from .services import *
from .db import Mydb
from .entity import *

db = Mydb()
user_service = UserService(UserModel(db))
config_service = ConfigService(ConfigModel(db))

