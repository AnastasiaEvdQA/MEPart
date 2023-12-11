import time

from pages.base_page import BasePage
from locators.basket_page_locators import BasketPageLocators as Locators
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC


class BasketPage(BasePage):

    def search_line(self):
        article_number = "A113707110CA"
        self.element_is_visible(Locators.SEARCH_FORM).send_keys(article_number)
        self.element_is_visible(Locators.FIND_BUTTON).click()

    def open_the_product_card(self):
        self.element_is_visible(Locators.SELECTED_PRODUCT).click()

    def add_product_to_cart(self):
        self.element_is_visible(Locators.ADD_TO_BASKET).click()
        self.element_is_visible(Locators.POPUP).click()

    def go_to_cart(self):
        self.element_is_visible(Locators.BASKET).click()

    def placing_an_order(self):
        name = "Test"
        phone = "9656589999"
        mail = "test@mail.ru"
        self.element_is_visible(Locators.CHECKOUT).click()
        self.element_is_visible(Locators.NAME).send_keys(name)
        self.element_is_visible(Locators.PHONE).send_keys(phone)
        self.element_is_visible(Locators.EMAIL).send_keys(mail)

    def choosing_a_delivery_method(self):
        # Выбор доставки
        self.element_is_visible(Locators.DELIVERY).click()

    def is_delivery_method_selected(self):
        # Вернуть True, если метод доставки курьером выбран, и False в противном случае
        return self.element_is_visible(Locators.DELIVERY).is_displayed()

    def choosing_a_payment_method(self):
        self.element_is_visible(Locators.PAYMENT_SELECTION).click()

    def is_payment_method_selected(self):
        # Вернуть True, если метод оплаты онлайн выбран, и False в противном случае
        return self.element_is_visible(Locators.PAYMENT_SELECTION).is_displayed()

    def proceed_to_checkout(self):
        self.element_is_visible(Locators.PAYMENT).click()

    def get_current_url(self):
        # Вернуть текущий URL страницы
        return self.driver.current_url

