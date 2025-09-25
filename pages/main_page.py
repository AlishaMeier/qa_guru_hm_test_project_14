import allure
from selene import browser, by, be, have


class MainPage:
    def __init__(self):
        # ... (остальные локаторы без изменений) ...
        self.destination_dropdown = browser.element('#b_s_c_container')
        self.search_button = browser.element('#b_s_submit')

        # --- ТОЧНЫЙ ЛОКАТОР для кнопки закрытия поп-апа ---
        self.luck_popup_close_button = browser.element('.fl-close-x')

    # --- Методы без изменений ---
    @allure.step("Выбрать страну назначения: {country_name}")
    def select_destination(self, country_name):
        pass

    @allure.step("Начать поиск туров")
    def search_tours(self):
        pass

    # --- ОБНОВЛЕННЫЙ МЕТОД для закрытия поп-апа ---
    @allure.step("Закрыть поп-ап 'Испытайте удачу', если он появился")
    def close_luck_popup_if_present(self):
        # Если кнопка закрытия существует на странице, нажать на нее.
        # Selene сама подождет появления элемента в течение таймаута.
        # Если элемент не появится, тест не упадет, а просто пойдет дальше.
        if self.luck_popup_close_button.with_(timeout=5).wait_until(be.visible):
            self.luck_popup_close_button.click()