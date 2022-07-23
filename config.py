from configparser import ConfigParser

class Config:

    __instance = None
    config_object = None

    @staticmethod
    def get_instance():
        if Config.__instance == None:
            Config()
        return Config.__instance

    """ Virtually private constructor. """
    def __init__(self):
        if Config.__instance != None:
            raise Exception("Class already instanciated. Class is a singleton.")
        else:
            Config.__instance = self
            Config.load_config_file(self)

    def load_config_file(self):
        self.config_object = ConfigParser()
        self.config_object.read("config.ini")

    def get_api_key(self):
        return self.config_object["API"]["api-key"]

    def get_user_key(self):
        return self.config_object["API"]["user-key"]
