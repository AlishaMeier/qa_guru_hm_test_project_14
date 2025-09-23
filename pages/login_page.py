from selene import browser, have, be
import allure


class LoginPage:

    def open(self):
        with allure.step("Открыть страницу логина"):
            browser.open("/login")
        return self

    def set_email(self, email):
        with allure.step(f"Ввести email: {email}"):
            browser.element('[data-testid="SIGN_IN_email"]').set_value(email)
        return self

    def set_password(self, password):
        with allure.step("Ввести пароль"):
            browser.element('[data-testid="SIGN_IN_password"]').set_value(password)
        return self

    def toggle_remember_me(self):
        with allure.step("Кликнуть по чекбоксу 'Выйти через 7 дней'"):
            browser.element('[name="remember_me"]').click()
        return self

    def submit(self):
        with allure.step("Нажать кнопку 'Продолжить'"):
            browser.element('[data-testid="SIGN_IN_submit"]').click()
        return self

    def should_see_error(self, message: str):
        with allure.step(f"Проверить сообщение об ошибке: {message}"):
            browser.all('[class*="error"]').element_by(have.exact_text(message)).should(be.visible)
        return self

    def should_be_logged_in(self):
        with allure.step("Проверить успешный вход (иконка профиля)"):
            browser.element('[data-testid="header-profile"]').should(be.visible)
        return self