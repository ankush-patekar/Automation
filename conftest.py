import time
import pytest
import json
from selenium import webdriver
from pages.base_page import BasePage
from locators.login_locators import LoginLocators

@pytest.fixture(scope="session")
def config():
    with open("config/test_data.json") as f:
        return json.load(f)


@pytest.fixture(scope="function")
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def login(browser, config):
    browser.get(config["url"])
    base_page = BasePage(browser)

    base_page.type(LoginLocators.USERNAME, config["username"])
    base_page.click(LoginLocators.CONTINUE, 5)
    base_page.type(LoginLocators.PASSWORD, config["password"])
    base_page.click(LoginLocators.LOGIN_BUTTON, 5)
    base_page.wait_for_page_load()
    time.sleep(2)
    assert "dashboard" in browser.current_url.lower()
    yield browser
