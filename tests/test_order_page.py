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
        order_page.click_to_element(MainPageLocators.BUTTON_ORDER_UP)
        order_page.set_order(data.NAME,
                             data.SURNAME,
                             data.ADDRESS,
                             data.NUM_STATION,
                             data.COLOR_SCOOTER,
                             data.DAYS_RENTAL,
                             data.COMMENT_FOR_COURIER)
        assert order_page.check_order() == data.CHECK_STATUS
        order_page.click_to_element(OrderPageLocators.BUTTON_CHECK_STATUS)
        order_page.find_element_with_wait(OrderPageLocators.BUTTON_CLOSE_ORDER)
        order_page.click_to_element(OrderPageLocators.BUTTON_LOGO_SCOOTER)
        assert order_page.current_url() == data.HOME_PAGE_URL

    @allure.title("Заказ самоката")
    @allure.description("Заказ самоката и переход на Яндекс Дзен")
    def test_order_scooter_and_transition_to_yandex_dzen(self, driver):
        order_page = OrderPage(driver)
        main_page = MainPage(driver)
        main_page.open_main_page_and_accepted_cookie()
        order_page.find_element_with_wait(MainPageLocators.BUTTON_ORDER_LOW)
        order_page.click_to_element(MainPageLocators.BUTTON_ORDER_LOW)
        order_page.set_order(data.NAME,
                             data.SURNAME,
                             data.ADDRESS,
                             data.NUM_STATION,
                             data.COLOR_SCOOTER,
                             data.DAYS_RENTAL,
                             data.COMMENT_FOR_COURIER)
        assert order_page.check_order() == data.CHECK_STATUS
        order_page.click_to_element(OrderPageLocators.BUTTON_CHECK_STATUS)
        order_page.find_element_with_wait(OrderPageLocators.BUTTON_CLOSE_ORDER)
        order_page.click_to_element(OrderPageLocators.BUTTON_FOR_TRANSITION_YA_DZEN)
        order_page.switch_to_next_tab()
        assert order_page.find_element_with_wait(OrderPageLocators.DZEN_PAGE_LOCATOR)
