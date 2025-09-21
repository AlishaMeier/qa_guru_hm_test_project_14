from selene.support.shared import browser
from selene import have

def test_homepage_title():
    browser.open("https://thetribe.com.cy/")
    browser.should(have.title_containing("The Tribe"))