from .models import ConfigModel
from .services import ConfigService
from .db import Mydb


db = Mydb()
config_service = ConfigService(ConfigModel(db))

