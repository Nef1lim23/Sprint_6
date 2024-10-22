import allure
import pytest
from selenium import webdriver

import data
from pages.main_page import MainPage


class TestMainPage:
    # driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()

    @pytest.mark.parametrize(
        'num, result',
        [
            (0, data.ANSWER_1),
            (1, data.ANSWER_2),
            (2, data.ANSWER_3),
            (3, data.ANSWER_4),
            (4, data.ANSWER_5),
            (5, data.ANSWER_6),
            (6, data.ANSWER_7),
            (7, data.ANSWER_8)
        ]
    )
    @allure.description("Проверка вопросов на главной странице")
    def test_questions_and_answers(self, driver, num, result):
        main_page = MainPage(driver)
        main_page.open_page(data.HOME_PAGE_URL)
        assert main_page.get_answer_text(num) == result

    @classmethod
    def teardown_class(cls):
        # закрыли браузер
        cls.driver.quit()
