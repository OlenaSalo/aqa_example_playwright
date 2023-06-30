import asyncio
import configparser
import os
import sys

import pytest
from playwright.sync_api import Page, sync_playwright

from src.app import Application

def pytest_addoption(parser):
    parser.addoption("--env", action="store", default="local", help="env variable name")


def read_ini():
    config_file = os.environ.get("config-file", "project-config.ini")
    root_path = os.path.join(sys.path[0], config_file)
    parser = configparser.ConfigParser()
    parser.read(root_path)
    return parser

@pytest.fixture
def get_config(request):
    env_name = request.config.getoption("--env")
    try:
        return read_ini()[env_name]
    except KeyError:
        raise Exception(f"Wrong configuration for env name [{env_name}] NOT present")


def remote_browser() -> Page:
     with sync_playwright() as pl:
        browser = pl.firefox.connect("http://moon.aerokube.local/wd/hub")
        context = browser.new_context()
        page = context.new_page()
     return page


async def remote_br() -> Page:
    async with sync_playwright() as pl:
        browser = await pl.firefox.connect("http://moon.aerokube.local/wd/hub")
        context = await browser.new_context()
        page = await context.new_page()
    return page


@pytest.fixture
def app(page: Page, get_config):

    return Application(page)

