import json
import os


def read_value_from_config(parameter):
    config_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '.env')
    with open(config_file_path) as config:
        file = json.load(config)
    try:
        return file[parameter]
    except KeyError:
        print("not found")