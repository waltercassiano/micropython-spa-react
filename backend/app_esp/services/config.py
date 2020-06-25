
class ConfigService:
    config_model = None

    def __init__(self, config_model):
        self.config_model = config_model

    def save_config_wifi(self, config_name, config_value):
        self.config_model.save("wifi_list", config_name, config_value)

    def get_config_wifi(self):
        return self.config_model.get("wifi_list")

    def save_active_user(self, config_name, config_value):
        self.config_model.save("logged_user", config_name, config_value)

    def get_active_user(self, config_name):
        return self.config_model.get("logged_user")
