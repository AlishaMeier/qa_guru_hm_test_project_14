import allure
from selene import browser, by, be, have


class MainPage:
    def __init__(self):
        self.popups_css = 'body > div'

    # --- Методы без изменений ---
    @allure.step("Выбрать страну назначения: {country_name}")
    def select_destination(self, country_name):
        pass

    @allure.step("Начать поиск туров")
    def search_tours(self):
        pass

    def close_all_popups(self):
        """
        Закрывает все поп-апы:
        - с кнопкой/крестиком
        - модалки подписки (кликаем вне зоны модалки)
        """
        while True:
            popups = browser.all(self.popups_css).filtered_by(be.visible)
            if not popups:
                break  # если нет видимых попапов — выходим

            for popup in popups:
                try:
                    # 1. пробуем закрыть кнопкой
                    close_button = popup.element('button, .close, .v-modal__close')
                    if close_button.matching(be.visible):
                        close_button.click()
                        popup.should(be.absent)
                        continue

                    # 2. если кнопки нет — кликаем в фон страницы
                    browser.element('body').click()
                    popup.should(be.absent)
                except Exception:
                    continue