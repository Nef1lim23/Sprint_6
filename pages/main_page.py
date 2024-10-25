import allure

import data
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step("получаем текст ответа под вопросом")
    def get_answer_text(self, num):
        locator_q_formatted = self.format_locators(MainPageLocators.QUESTION_LOCATOR, num)
        locator_a_formatted = self.format_locators(MainPageLocators.ANSWER_LOCATOR, num)
        self.scroll_to_element(MainPageLocators.QUESTION_LOCATOR_8)
        self.click_to_element(locator_q_formatted)
        return self.get_text_from_element(locator_a_formatted)

    @allure.step("Переходим на основную страницу и принимаем куки")
    def open_main_page_and_accepted_cookie(self):
        self.open_page(data.HOME_PAGE_URL)
        self.click_to_element(MainPageLocators.ACCEPT_COOKIE_BUTTON)

    @allure.step("кликаем на кнопку перехода на главную страницу самоката")
    def click_to_logo_scooter(self):
        self.click_to_element(MainPageLocators.BUTTON_LOGO_SCOOTER)

    @allure.step("Кликаем на кнопку 'заказать' вверху страницы")
    def click_to_button_order_up(self):
        self.click_to_element(MainPageLocators.BUTTON_ORDER_UP)

    @allure.step("Кликаем на кнопку 'заказать' внизу страницы")
    def click_to_button_order_low(self):
        self.click_to_element(MainPageLocators.BUTTON_ORDER_LOW)
