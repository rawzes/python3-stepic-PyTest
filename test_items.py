import time

from selenium.webdriver.common.by import By
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_add_to_basket_button(browser):
    browser.get(link)
    button = browser.find_elements(By.CSS_SELECTOR, "button.btn-add-to-basket")
    assert len(button) == 1, "Button is not displayed"
