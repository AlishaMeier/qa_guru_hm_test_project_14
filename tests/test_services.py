import allure
from pages.main_page import MainPage
from selene.support.shared import browser
from selene import be

@allure.title("The Services section is displayed.")
def test_services_section():
    MainPage().open().click_services()
    browser.element('#services').should(be.visible)