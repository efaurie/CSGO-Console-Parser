import os
import ConfigParser

class ConsoleParserConfigReader:

    def __init__(self, config_path):
        self.config_path = config_path
        self.config = self.read_config(config_path)

    @staticmethod
    def read_config(config_path):
        config = ConfigParser.ConfigParser()
        config.read(config_path)
        return config

    @property
    def log_location(self):
        raw_location = self.config.get('CSGO Settings', 'LogLocation')
        return os.path.normpath(raw_location)
