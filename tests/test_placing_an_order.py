from pages.basket_page import BasketPage


class TestBasketPage:

    def test_serch_string(self, driver):
        basket_page = BasketPage(driver, 'https://dev.mepart.ru/personal/cart/')
        # Открываем страницу магазина в браузере
        basket_page.open()
        # Находим строку поиска и вводим артикул товара
        basket_page.search_line()
        # Выбираем и открываем карточку товара с артикулом A113707110CA  и брендом CHERY
        basket_page.open_the_product_card()
        # Добавляем товар в корзину
        basket_page.add_product_to_cart()
        # Переходим в корзину
        basket_page.go_to_cart()
        # Оформление заказа
        basket_page.placing_an_order()
        #Выбор доставки
        basket_page.choosing_a_delivery_method()
        assert basket_page.is_delivery_method_selected(), "Доставка курьером не была выбрана!"
        #Выбор оплаты
        basket_page.choosing_a_payment_method()
        assert basket_page.is_payment_method_selected(), "Оплата онлайн не была выбрана!"
        # переход на страницу оплаты
        basket_page.proceed_to_checkout()
        # Получение текущего URL
        current_url = basket_page.get_current_url()
        # Проверка, что текущий URL соответствует ожидаемому URL страницы оплаты
        expected_payment_url = "https://pay.payonline.ru/"
        assert current_url == expected_payment_url, "Переход на страницу оплаты не выполнен!"






