import allure
from selene.support.shared import browser
from selene import have

@allure.title("All images on the main page have been uploaded.")
def test_images_loaded():
    browser.open("/")
    images = browser.all('img')
    for img in images:
        img.should(have.attribute('src'))