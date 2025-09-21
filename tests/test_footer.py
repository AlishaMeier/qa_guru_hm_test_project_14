import allure
from selene.support.shared import browser
from selene import have, be

@allure.title("The footer is visible on the main page.")
def test_footer_visible():
    browser.open("/")
    browser.element('footer').should(be.visible)

@allure.title("Checking links in the footer")
def test_footer_links():
    browser.open("/")
    links = browser.all('footer a')
    for link in links:
        link.should(have.attribute('href'))