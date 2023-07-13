import asyncio
import configparser
import os
import sys

import pytest
from playwright.sync_api import sync_playwright

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

@pytest.fixture(scope="session")
def browser(request):
    with sync_playwright() as playwright:
        browser = playwright[get_config(request)['browser_name']].launch(headless=False)
        yield browser
        browser.close()

@pytest.fixture(scope="session")
def page(request, browser):
    context = browser.new_context()
    page = context.new_page()
    page.goto(get_config(request)['base_url'])
    yield page
    context.close()

@pytest.fixture
def app(page, request):
    return Application(page, get_config(request)['base_url'])

