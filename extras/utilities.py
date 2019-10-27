import json
from config import ApplicationConfig


class Utilities:

    @staticmethod
    def read_data_file(filename, path):
        with open(ApplicationConfig.PROJECT_ROOT + path + filename) as data_file:
            return json.load(data_file)
