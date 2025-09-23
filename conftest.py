import pytest
import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import InvalidSessionIdException, WebDriverException
from selene import browser
from utils import attach


@pytest.fixture(scope="session", autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope="function")
def remote_browser_setup():
    selenoid_login = os.getenv("SELENOID_LOGIN")
    selenoid_pass = os.getenv("SELENOID_PASS")
    selenoid_url = os.getenv("SELENOID_URL")  # например: selenoid.company.com:4444

    options = Options()
    options.set_capability("goog:loggingPrefs", {"browser": "ALL"})

    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "128.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True,
        },
    }

    options.capabilities.update(selenoid_capabilities)

    # собираем правильный url
    command_executor = f"http://{selenoid_login}:{selenoid_pass}@{selenoid_url}/wd/hub"

    driver = webdriver.Remote(
        command_executor=command_executor,
        options=options,
    )

    browser.config.driver = driver
    yield browser

    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_screenshot(browser)
    attach.add_video(browser)

    try:
        browser.quit()
    except (InvalidSessionIdException, WebDriverException):
        pass


@pytest.fixture(autouse=True)
def setup_browser(remote_browser_setup):
    base_url = os.getenv("BASE_URL", "https://capital.com/ru-int")
    browser.config.base_url = base_url
    browser.config.timeout = 5
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    yield