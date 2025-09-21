import allure
from selene.support.shared import browser
from selene import have, be

@allure.title("The Contact button is visible and clickable.")
def test_contact_button():
    browser.open("https://thetribe.com.cy/")
    browser.element('a[href="#contact"]').should(be.visible).click()
    browser.should(have.url_containing("#contact"))