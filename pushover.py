from chump import Application
from config import get_api_key, get_user_key

def initialize():
    app = Application(get_api_key())
    user = app.get_user(get_user_key())
    return user

def notify(utilisateur, message):
    message = utilisateur.create_message(message)
    message.send()
