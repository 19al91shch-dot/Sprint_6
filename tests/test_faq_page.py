import pytest
import allure 

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from locators.faq_locators import FaqPageLocators
from page_objects.faq_page import FaqPage
from page_objects.main_page import BasePage
from urls import MAIN_URL
from test_data.faq_data import FAQ_DATA


class TestFaqPage:

    @pytest.mark.parametrize(
        'question_locator, answer_locator, expected_text, test_id',
        FAQ_DATA,
        ids=[item[3] for item in FAQ_DATA]
    )
    @allure.title("FAQ: ответ на вопрос '{test_id}' соответствует ожидаемому")
    @allure.description(
        "Проверка, что при клике на вопрос в разделе FAQ "
        "ответ раскрывается и текст ответа совпадает с ожидаемым."
    )
    def test_faq_question_opens_and_shows_correct_answer(
            self, driver, question_locator, answer_locator, expected_text, test_id
    ):
        faq_page = FaqPage(driver)
        faq_page.open()
        faq_page.accept_cookies()
        faq_page.scroll_to_faq_section()

        is_answer_visible = faq_page.open_question_and_wait_answer(
            question_locator, answer_locator
        )

        assert is_answer_visible, f"Ответ на вопрос '{test_id}' не отображается"

        answer_text = faq_page.get_text_from_element(answer_locator)

        assert answer_text == expected_text, (
            f"Некорректный текст ответа на вопрос '{test_id}'. "
            f"Ожидалось: {expected_text!r}. "
            f"Получено: {answer_text!r}"
        )
        