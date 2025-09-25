# conftest.py
import os
import pytest
from dotenv import load_dotenv
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from utils import attach

@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()

@pytest.fixture(scope='function', autouse=True)
def setup_browser():
    options = Options()
    chrome_options.add_argument("--disable-notifications")  # иногда работает
    chrome_prefs = {"profile.default_content_setting_values.notifications": 2}
    selenoid_url = os.getenv("SELENOID_URL")
    selenoid_login = os.getenv("SELENOID_LOGIN")
    selenoid_pass = os.getenv("SELENOID_PASS")

    if selenoid_url:
        # Настройка для удаленного запуска в Selenoid
        selenoid_capabilities = {
            "browserName": "chrome",
            "browserVersion": "128.0", # Укажите нужную версию
            "selenoid:options": {
                "enableVNC": True,
                "enableVideo": True
            }
        }
        options.capabilities.update(selenoid_capabilities)
        remote_url = f"https://{selenoid_login}:{selenoid_pass}@{selenoid_url}/wd/hub"
        driver = webdriver.Remote(command_executor=remote_url, options=options)
    else:
        # Локальный запуск
        driver = webdriver.Chrome(options=options)

    browser.config.driver = driver
    browser.config.base_url = os.getenv('BASE_URL')
    browser.config.timeout = 5.0
    browser.config.window_width = 1920
    browser.config.window_height = 1080

    yield browser

    # Логика, которая выполнится после каждого теста
    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    if selenoid_url:
        attach.add_video(browser)

    browser.quit()