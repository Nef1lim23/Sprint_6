import allure
import pytest


import data
from pages.main_page import MainPage


class TestMainPage:

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
    @allure.title("Проверка вопросов на главной странице")
    def test_questions_and_answers(self, driver, num, result):
        main_page = MainPage(driver)
        main_page.open_main_page_and_accepted_cookie()
        assert main_page.get_answer_text(num) == result
