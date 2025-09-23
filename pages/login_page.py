import allure
from selene import browser, have, be
from selenium.common.exceptions import WebDriverException


class CapitalLoginPage:

    def open(self):
        with allure.step("Open Capital.com"):
            # сначала открываем базовый раздел, чтобы элементы в хедере отрендерились
            browser.open("/ru-int")
            # попытка кликнуть на хедер кнопку "Войти" / link to login
            try:
                # сначала универсальный href
                header_btn = browser.element('a[href*="/login"]')
                if header_btn.matching(be.visible).exists():
                    header_btn.click()
                else:
                    # fallback: кнопка с текстом "Войти" (xpath)
                    browser.element('//button[contains(normalize-space(.),"Войти")]').click()
            except WebDriverException:
                # если не получилось — открыть страницу логина напрямую
                browser.open("/ru-int/login")

            # Ждём появления поля email (формы)
            browser.element('[data-testid="SIGN_IN_email"]').should(be.visible)
        return self

    def set_email(self, email: str):
        with allure.step(f"Filled: {email}"):
            browser.element('[data-testid="SIGN_IN_email"]').should(be.visible).set_value(email)
        return self

    def set_password(self, password: str):
        with allure.step("Filled password"):
            browser.element('[data-testid="SIGN_IN_password"]').should(be.visible).set_value(password)
        return self

    def toggle_remember_me(self):
        with allure.step("Click remembering checkbox"):
            browser.element('input[name="remember_me"]').click()
        return self

    def submit(self):
        with allure.step("Click button 'Продолжить'"):
            browser.element('[data-testid="SIGN_IN_submit"]').should(be.visible).click()
        return self

    def login(self, email: str, password: str, remember: bool = False):
        self.open()
        self.set_email(email)
        self.set_password(password)
        if remember:
            self.toggle_remember_me()
        self.submit()
        return self

    def should_be_logged_in(self):
        with allure.step("Check login (userpic is available)"):
            possible = '[data-testid="header-profile"], [data-testid="header-user"], .user-avatar, .header-profile'
            browser.element(possible).should(be.visible)
        return self

    def should_see_error(self, message: str):
        with allure.step(f"Проверить сообщение об ошибке: '{message}'"):
            error_selectors = '[data-error="true"], .toast, [role="alert"], .validation-error, .input__error'
            browser.element(error_selectors).should(have.text(message))
        return self
