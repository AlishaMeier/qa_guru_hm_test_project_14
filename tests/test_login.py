import os
import allure
from allure_commons.types import Severity
from selene import browser
# Убедитесь, что импорты соответствуют именам ваших файлов
from pages.login_page import LoginPage
from pages.main_page import MainPage

@allure.tag("WEB")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "your_github_nickname")
@allure.feature("Авторизация")
@allure.story("Успешный вход зарегистрированного пользователя")
@allure.title("Проверка авторизации на fstravel.com")
def test_successful_login(setup_browser):
    # Создаем экземпляры ВСЕХ нужных страниц в начале
    login_page = LoginPage()
    main_page = MainPage() # <-- ВОТ РЕШЕНИЕ

    # Данные из .env файла
    login_email = os.getenv('FSTRAVEL_USER_EMAIL')
    login_password = os.getenv('FSTRAVEL_USER_PASSWORD')

    with allure.step("Открыть главную страницу"):
        browser.open('/')

    with allure.step("Закрываем поп-ап 'Колесо удачи', если он появился"):
        main_page.close_luck_popup_if_present() # <-- Теперь эта строка сработает

    with allure.step("Выполнить вход в систему"):
        login_page.login(login_email, login_password)

    with allure.step("Проверить, что авторизация прошла успешно"):
        login_page.user_should_be_logged_in()