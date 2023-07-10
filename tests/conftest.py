import asyncio
import configparser
import os
import sys

import pytest

from src.app import Application

def pytest_addoption(parser):
    parser.addoption("--env", action="store", default="local", help="env variable name")


def read_ini():
    config_file = os.environ.get("config-file", "project-config.ini")
    root_path = os.path.join(sys.path[0], config_file)
    parser = configparser.ConfigParser()
    parser.read(root_path)
    return parser


def get_config(request):
    env_name = request.config.getoption("--env")
    try:
        return read_ini()[env_name]
    except KeyError:
        raise Exception(f"Wrong configuration for env name [{env_name}] NOT present")

@pytest.fixture
def app(page, request):
    return Application(page, get_config(request)['base_url'])

