from datetime import datetime
import allure
import data
import helper

from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class OrderPage(BasePage):

    @staticmethod
    def get_locator_by_color(color):
        if color == 'black':
            return OrderPageLocators.COLOR_SCOOTER_BLACK
        elif color == 'grey':
            return OrderPageLocators.COLOR_SCOOTER_GREY
        else:
            raise ValueError(f"Некорректный цвет: {color}. Допустимые значения: 'black' или 'grey'")

    def select_current_day(self):
        # Получаем текущую дату
        current_date = datetime.now()
        self.find_element_with_wait(OrderPageLocators.DATE_WHEN_TO_BRING_SCOOTER)
        self.click_to_element(OrderPageLocators.DATE_WHEN_TO_BRING_SCOOTER)
        self.find_element_with_wait(OrderPageLocators.CALENDAR_FIELD)
        # Формируем локатор для ячейки с текущим днем
        date_cell_locator = self.format_locators(OrderPageLocators.CALENDAR_CLICK_ON_DATA, current_date.day)
        self.find_element_with_wait(date_cell_locator)
        self.click_to_element(date_cell_locator)

    @allure.step("Создаем заказ с переданными параметрами")
    def set_order(self, name, surname, address, num_station, color, days_rental, comment_for_courier):

        #Ввод имя, фамилия и адрес
        self.add_text_to_element(OrderPageLocators.NAME_INPUT_FIELD, name)
        self.add_text_to_element(OrderPageLocators.SURNAME_INPUT_FIELD, surname)
        self.add_text_to_element(OrderPageLocators.ADDRESS_INPUT_FIELD, address)
        #Выбора станции метро
        self.click_to_element(OrderPageLocators.METRO_STATION_FIELD)
        select_station = self.format_locators(OrderPageLocators.METRO_STATION_LIST, num_station)
        self.click_to_element(select_station)
        #ввод телефона с функцией рандомного номера
        self.add_text_to_element(OrderPageLocators.TELEPHONE_INPUT_FIELD, helper.generate_phone_number())
        #Кликаем на переход на следующую страницу заказа
        self.click_to_element(OrderPageLocators.BUTTON_NEXT)
        #Ожидание пока прогрузится вторая часть заказа
        self.find_element_with_wait(OrderPageLocators.DATE_WHEN_TO_BRING_SCOOTER)
        #тут по идее в поле дата должна вводиться дата сегодня чтобы тест был актуален
        self.select_current_day()
        #далее идет функционал выбора длительности ренты
        self.click_to_element(OrderPageLocators.RENTAL_PERIOD_FIELD)
        rental_period = self.format_locators(OrderPageLocators.TIME_RENTAL_SCOOTER, days_rental)
        self.click_to_element(rental_period)
        #Далее вариант выбора цвета самоката, тут лучше, как по мне, вызвать метод в тесте отдельно и указать че куда
        color_test = OrderPage.get_locator_by_color(color)
        self.click_to_element(color_test)
        #добавление комментария для курьерчика
        self.add_text_to_element(OrderPageLocators.COMMENT_FOR_COURIER, comment_for_courier)
        self.click_to_element(OrderPageLocators.BUTTON_ORDER_FROM_FORM_ORDER)
        self.find_element_with_wait(OrderPageLocators.FORM_ACCEPTED_ORDER)
        self.click_to_element(OrderPageLocators.BUTTON_YES)

    @allure.step("Проверяем статус заказа")
    def check_order(self):
        return self.get_text_from_element(OrderPageLocators.BUTTON_CHECK_STATUS)

    @allure.step("Переключаемся на открытую вкладку")
    def switch_to_next_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.wait_url_to_be(data.PAGE_YA_DZEN)
