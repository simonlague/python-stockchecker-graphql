from chump import Application
from config import Config

class Notification:

    __user = None

    def __init__(self):
        self.__user = self.initialize()

    def initialize(self):
        config = Config.get_instance()
        app = Application(config.get_api_key())
        return app.get_user(config.get_user_key())

    def notify(self, message):
        message = self.__user.create_message(message)
        message.send()
