from chump import Application
from config import Config

class Notification:

    user = None

    def __init__(self):
        self.user = self.initialize()

    def initialize(self):
        config = Config.get_instance()
        app = Application(config.get_api_key())
        user = app.get_user(config.get_user_key())
        return user

    def notify(self, message):
        message = self.user.create_message(message)
        message.send()
