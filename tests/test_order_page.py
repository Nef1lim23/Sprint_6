import allure
import data
from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderPageLocators
from pages.main_page import MainPage
from pages.order_page import OrderPage


class TestOrderPage:

    @allure.title("Заказ самоката")
    @allure.description("Тест по созданию заказа и перехода на главную страницу")
    def test_order_scooter_and_return_to_the_main_page(self, driver):
        order_page = OrderPage(driver)
        main_page = MainPage(driver)
        main_page.open_main_page_and_accepted_cookie()
        main_page.click_to_button_order_up()
        order_page.set_order(data.NAME,
                             data.SURNAME,
                             data.ADDRESS,
                             data.NUM_STATION,
                             data.COLOR_SCOOTER,
                             data.DAYS_RENTAL,
                             data.COMMENT_FOR_COURIER)
        assert order_page.check_order() == data.CHECK_STATUS
        order_page.check_status_and_close_order()
        main_page.click_to_logo_scooter()
        assert order_page.current_url() == data.HOME_PAGE_URL

    @allure.title("Заказ самоката")
    @allure.description("Заказ самоката и переход на Яндекс Дзен")
    def test_order_scooter_and_transition_to_yandex_dzen(self, driver):
        order_page = OrderPage(driver)
        main_page = MainPage(driver)
        main_page.open_main_page_and_accepted_cookie()
        main_page.click_to_button_order_low()
        order_page.set_order(data.NAME_2,
                             data.SURNAME_2,
                             data.ADDRESS_2,
                             data.NUM_STATION_2,
                             data.COLOR_SCOOTER_2,
                             data.DAYS_RENTAL_2,
                             data.COMMENT_FOR_COURIER_2)
        assert order_page.check_order() == data.CHECK_STATUS
        order_page.check_status_and_close_order()
        order_page.click_on_button_transition_ya_dzen()
        order_page.switch_to_next_tab()
        assert order_page.find_element_with_wait(OrderPageLocators.DZEN_PAGE_LOCATOR)
