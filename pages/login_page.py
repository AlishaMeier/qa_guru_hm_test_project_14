from selene import browser, by, be
import allure

class LoginPage:
    def __init__(self):
        self.header_login_icon = browser.element('.v-icon-user-14')
#        self.modal = browser.element('.div-modal.div-modal-auth-new')
        self.email_input = browser.element('#email')
        self.password_input = browser.element('#password')
        self.submit_button = browser.element('form input[type="submit"]')

    @allure.step("Выполняем вход пользователя с email: {email}")
    def login(self, email, password):
        # Открываем модальное окно по клику на иконку
        self.header_login_icon.click()
        self.modal.should(be.visible)

        # Заполняем форму и отправляем
        with allure.step(f'Вводим email: {email}'):
            self.email_input.type(email)
        with allure.step('Вводим пароль'):
            self.password_input.type(password)
        with allure.step('Нажимаем кнопку "Войти"'):
            self.submit_button.click()

    @allure.step("Проверяем, что пользователь успешно авторизован")
    def user_should_be_logged_in(self):
        # После успешного входа вместо иконки входа появляется иконка с аватаром
        # У этой иконки будет другой класс или атрибут, который нужно проверить
        # Например, можно проверить, что старая иконка исчезла
        self.header_login_icon.should(be.not_.visible)
        # ИЛИ, что более надежно, проверить появление ссылки на "Личный кабинет"
        browser.element(by.text('Личный кабинет')).should(be.visible)