from configparser import ConfigParser

def load_config():
    config_object = ConfigParser()
    config_object.read("config.ini")
    return config_object

config = load_config()

def get_api_key():
    config_api = config["API"]
    return config_api["api-key"]

def get_user_key():
    config_api = config["API"]
    return config_api["user-key"]
