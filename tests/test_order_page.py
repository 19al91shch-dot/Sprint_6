import pytest
import allure

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators.order_locators import OrderPageLocators
from locators.main_locators import MainPageLocators
from urls import MAIN_URL, ORDER_URL, DZEN_URL
from page_objects.main_page import BasePage
from page_objects.order_page import OrderPage


class TestOrderPage:


    @pytest.mark.parametrize("name,surname,address,station_name,phone_number,date_str, days_text, color_name, comment_text",
                             [("Алёна", "Иванова", "пр. Правды, 25", "Чистые пруды", "87777777777"
                             "", "10.11.2026", "семеро суток", "чёрный жемчуг", "Позвонить заранее"),
                              ("Иван", "Петров", "ул. Комсомольская, 7", "Комсомольская", "89998880000", "15.11.2026", "сутки", "серая безысходность", "Не звонить, писать на What")])
    @allure.title("Позитивный сценарий: заказ через верхнюю кнопку 'Заказать'")
    @allure.description("Проверяет заполнение формы и появление всплывающего окна об успешном заказе.")
    def test_order_via_top_button(self, driver, name, surname, address, station_name, phone_number, date_str, days_text, color_name, comment_text):
        main_page = BasePage(driver)
        order_page = OrderPage(driver)
        main_page.open()
        main_page.accept_cookies()
        order_page.open_from_main_page()
        order_page.fill_first_order_form(name, surname, address, station_name, phone_number)
        order_page.click_submit_button()
        order_page.fill_second_order_form(date_str, days_text, color_name, comment_text)
        order_page.click_order_button_in_form()
        message = order_page.complete_order_confirmation()

        assert "Заказ оформлен" in message


    @pytest.mark.parametrize("name,surname,address,station_name,phone_number,date_str, days_text, color_name, comment_text",
                             [("Серик", "Сериков", "ул. Космонавтов, 77", "Алма-Атинская", "88885566777", "12.11.2026", "трое суток", "чёрный жемчуг", "Привезти в обеденное время"),
                              ("Павел", "Павлов", "ул. Октябрьская, 44", "Красные Ворота", "87772222333", "13.11.2026", "двое суток", "серая безысходность", "")])
    @allure.title("Позитивный сценарий: заказ через нижнюю кнопку 'Заказать'")
    @allure.description("Проверяет заполнение формы и появление всплывающего окна об успешном заказе.")
    def test_order_via_bottom_button(self, driver, name, surname, address, station_name, phone_number, date_str, days_text, color_name, comment_text):
        main_page = BasePage(driver)
        order_page = OrderPage(driver)
        main_page.open()
        main_page.accept_cookies()
        order_page.scroll_to_bottom_order_button()
        order_page.click_bottom_order_button()
        order_page.fill_first_order_form(name, surname, address, station_name, phone_number)
        order_page.click_submit_button()
        order_page.fill_second_order_form(date_str, days_text, color_name, comment_text)
        order_page.click_order_button_in_form()
        message = order_page.complete_order_confirmation()

        assert "Заказ оформлен" in message


    @allure.title("Проверка клика по логотипу 'Самокат'")
    @allure.description("При клике по логотипу 'Самокат' на странице заказа происходит переход на главную страницу сервиса.")
    def test_click_scooter_logo(self, driver):
        order_page = OrderPage(driver)
        order_page.open()
        order_page.accept_cookies()
        order_page.wait_for_scooter_logo()
        order_page.click_scooter_logo()

        assert order_page.is_on_main_page(MAIN_URL)


    @allure.title("Проверка клика по логотипу 'Яндекс'")
    @allure.description("При клике по логотипу 'Яндекс' открывается Дзен в новой вкладке.")
    def test_click_yandex_logo(self, driver):
        order_page = OrderPage(driver)
        order_page.open()
        order_page.accept_cookies()
        order_page.click_yandex_logo()
        order_page.wait_for_new_tab()
        order_page.switch_to_last_tab()
        order_page.wait_url_contains("dzen.ru")

        assert "dzen.ru" in order_page.get_current_url()