import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from  selenium.common.exceptions import TimeoutException

from urls import MAIN_URL
from locators.faq_locators import FaqPageLocators
from page_objects.main_page import BasePage


class FaqPage(BasePage):
    @allure.step("Открытие страницы FAQ")
    def open(self):
        super().open(MAIN_URL)

    @allure.step("Прокрутка до секции FAQ")
    def scroll_to_faq_section(self):
        self.scroll_to_element(FaqPageLocators.FAQ_SECTION)

    @allure.step("Получение текста элемента с локатором {locator}")
    def get_text_from_element(self, locator, timeout=10):
        return self._wait_for_element(locator, timeout).text

    @allure.step("Проверка, что ответ стал видимым")
    def check_is_answer_visible(self, answer_locator, timeout=10):
        try:
            element = self._wait_for_element(answer_locator, timeout)
            return element.is_displayed()
        except TimeoutException:
            return False

    @allure.step("Открытие вопроса и ожидание отображения ответа")
    def open_question_and_wait_answer(
            self, question_locator, answer_locator, timeout=10
    ):
        self.click_element(question_locator, timeout)
        return self.check_is_answer_visible(answer_locator, timeout)

    