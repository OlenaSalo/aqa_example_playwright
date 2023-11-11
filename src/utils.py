import json
import logging
import os
import sys

LOG = logging.getLogger()
path = os.path.join(sys.path[0], "account.json")

def parse_json(json_file: str)-> dict:
    try:
        with open(path) as data_file:
            data: dict = json.load(data_file)
        return data
    except FileNotFoundError:
        LOG.error(f"File {json_file} not exist")
