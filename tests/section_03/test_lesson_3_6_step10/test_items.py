import time
from selenium.webdriver.common.by import By


def test_button_add_to_cart(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

    browser.get(link)
    button = browser.find_element(By.CSS_SELECTOR, '.btn.btn-lg.btn-primary.btn-add-to-basket')
    button_to_cart_expected = 'submit'
    button_to_cart_actual = button.get_attribute('type')

    assert button_to_cart_expected == button_to_cart_actual, \
        f"The expected button is '{button_to_cart_expected}', but it is '{button_to_cart_actual} ir absent"   
    
    time.sleep(5)
