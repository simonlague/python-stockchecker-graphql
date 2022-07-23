from chump import Application
from config import Config

def initialize():
    config = Config.get_instance()
    app = Application(config.get_api_key())
    user = app.get_user(config.get_user_key())
    return user

def notify(utilisateur, message):
    message = utilisateur.create_message(message)
    message.send()
