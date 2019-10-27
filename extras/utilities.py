import json
import logging
from config import ApplicationConfig


class Utilities:

    @staticmethod
    def read_data_file(filename, path):
        file = ApplicationConfig.PROJECT_ROOT + path + filename
        logging.info("Getting ready to read from:" + file)
        with open(file) as data_file:
            return json.load(data_file)

    @staticmethod
    def convert_to_json(result, description):
        logging.info("Converting the result to JSON")
        row_headers = [x[0] for x in description]
        json_data = []
        for row in result:
            json_data.append(dict(zip(row_headers, row)))
        return json.dumps(json_data)
