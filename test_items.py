import time

from selenium.webdriver.common.by import By


def test_add_to_cart_button_is_present(browser):
    browser.get('https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
    add_to_cart_button = browser.find_element(
        By.CSS_SELECTOR, 'button.btn-add-to-basket'
    )
    assert add_to_cart_button.is_displayed(), f'Page should have {add_to_cart_button}'

    time.sleep(30)
