import pandas as pd
import os
import json


def read_json(file_path):
    file = open(file_path, "r")
    return json.load(file)


file_path = os.path.join('./', 'data', 'locations', 'output_4.json')
json_contents = read_json(file_path)


def read_all_json_files(JSON_ROOT):
    my_list = []

    for name in os.listdir(JSON_ROOT):
        path = os.path.join(JSON_ROOT, name)

        if os.path.isfile(path):
            my_list.append(read_json(path))
    return my_list


df = read_all_json_files('./data/locations')


print(json_contents)