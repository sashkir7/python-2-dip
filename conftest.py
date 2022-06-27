import pytest
from selene.support.shared import browser


@pytest.fixture(scope='session', autouse=True)
def set_browser_size():
    browser.config.window_width = 1920
    browser.config.window_height = 1080


@pytest.fixture()
def open_google():
    browser.open("https://google.com")
