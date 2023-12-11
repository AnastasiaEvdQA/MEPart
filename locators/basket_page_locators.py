from selenium.webdriver.common.by import By


class BasketPageLocators:
    SEARCH_FORM = (By.CSS_SELECTOR, "#input-autocomplit")
    FIND_BUTTON = (By.CSS_SELECTOR, "#input-autocomplit-submit")
    SELECTED_PRODUCT = (By.CSS_SELECTOR, 'body > main > div > div.row.flex-nowrap.main-filter-wrapper > div > div:nth-child(2) > a > div.col-brend > div > span')
    ADD_TO_BASKET = (By.CSS_SELECTOR, '#arProduct > div.row.d-flex.table_row_search.first-row > div.col-cart.mt-2.mt-lg-0 > a')
    POPUP = (By.CSS_SELECTOR, '#basket-add-popup-submit')
    BASKET = (By.CSS_SELECTOR, 'body > header > div.container.bot-row > div > div.col-xl-3.col-md-6.order-md-1.col-6.order-1.header-tablet-col-6.header-tablet-order-1 > div > div.bot.d-flex.align-items-start.justify-content-between > a.d-flex.flex-column.align-items-center.justify-content-center.cart-link')
    CHECKOUT = (By.CSS_SELECTOR, 'body > main > div > div.row.cart-row.cart_ajax > div.col-xl-3.order-xl-1.col-md-12.order-md-0.col-12.order-0.tablet-col.tablet-col-order-0 > div > div > form > div.sub-row.d-flex.align-items-center.justify-content-lg-center.justify-content-md-start > button')
    NAME = (By.CSS_SELECTOR, '#orderForm > div > div.col-12.col-md-8 > div:nth-child(1) > div > div > div:nth-child(1) > input')
    PHONE = (By.CSS_SELECTOR, '#orderForm > div > div.col-12.col-md-8 > div:nth-child(1) > div > div > div:nth-child(2) > input')
    EMAIL = (By.CSS_SELECTOR, '#orderForm > div > div.col-12.col-md-8 > div:nth-child(1) > div > div > div:nth-child(3) > input')
    DELIVERY = (By.CSS_SELECTOR, '#orderForm > div > div.col-12.col-md-8 > div:nth-child(2) > div > div > div.col-12.col-md-4 > div > div:nth-child(2) > input[type="checkbox"]')
    PAYMENT_SELECTION = (By.CSS_SELECTOR, '#PAY_SYSTEM_4')
    PAYMENT = (By.CSS_SELECTOR, '#orderForm > div > div.col-12.col-md-8 > div.row.my-2 > div > button')
    NAME_OF_PRODUCT = (By.CSS_SELECTOR, 'h1[class*=font-weight-light]')
