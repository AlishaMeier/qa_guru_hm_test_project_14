import os
import pytest
import allure
from pages.login_page import LoginPage


@allure.epic("Login")
@allure.feature("Authorization via Email")
class TestLogin:

    @allure.story("Succesful login")
    def test_successful_login(self):
        login_page = LoginPage()
        login_page.open() \
            .set_email(os.getenv("TEST_USER_EMAIL")) \
            .set_password(os.getenv("TEST_USER_PASSWORD")) \
            .submit() \
            .should_be_logged_in()

    @allure.story("Invalid password")
    def test_invalid_password(self):
        login_page = LoginPage()
        login_page.open() \
            .set_email(os.getenv("TEST_USER_EMAIL")) \
            .set_password("wrong_password") \
            .submit() \
            .should_see_error("Неверный логин или пароль")

    @allure.story("Empty email field")
    def test_empty_email(self):
        login_page = LoginPage()
        login_page.open() \
            .set_password("some_password") \
            .submit() \
            .should_see_error("Введите адрес электронной почты")

    @allure.story("Empty pass field")
    def test_empty_password(self):
        login_page = LoginPage()
        login_page.open() \
            .set_email(os.getenv("TEST_USER_EMAIL")) \
            .submit() \
            .should_see_error("Введите пароль")

    @allure.story("Invalid email")
    def test_invalid_email_format(self):
        login_page = LoginPage()
        login_page.open() \
            .set_email("invalid@") \
            .set_password("some_password") \
            .submit() \
            .should_see_error("Введите корректный адрес электронной почты")

    @allure.story("Checkbox 'Выйти через 7 дней'")
    def test_toggle_remember_me(self):
        login_page = LoginPage()
        login_page.open() \
            .set_email(os.getenv("TEST_USER_EMAIL")) \
            .set_password(os.getenv("TEST_USER_PASSWORD")) \
            .toggle_remember_me() \
            .submit() \
            .should_be_logged_in()

    @allure.story("Link 'Забыли пароль?'")
    def test_forgot_password_link(self):
        login_page = LoginPage()
        login_page.open()
        with allure.step("Кликнуть 'Забыли пароль?' и проверить переход"):
            from selene import browser, be
            browser.element('[data-testid="SIGN_IN_forgot_link"]').click()
            browser.should(have.url_containing("/reset-password"))
