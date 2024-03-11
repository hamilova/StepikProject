from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_URL = (By.PARTIAL_LINK_TEXT, "login")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    ADD_ITEM_TO_THE_BASKET_LINK = (By.CSS_SELECTOR, "button.btn-add-to-basket:nth-child(3)")
    CART_LINK = (By.CSS_SELECTOR, ".btn[href='/en-gb/basket/']:nth-child(1)")
    ITEM_IN_BASKET = (By.CSS_SELECTOR, 'h3 a[href="/en-gb/catalogue/the-shellcoders-handbook_209/"]')
    ITEM_ADDED_MESSAGE = (By.CSS_SELECTOR, '.alertinner:first-of-type')
    PRODUCT_NAME = (By.CSS_SELECTOR, 'div h1')
    PRODUCT_NAME_IN_BASKET = (By.CSS_SELECTOR, "div h3 a")