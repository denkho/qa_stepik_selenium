import math
import os
import time
import pytest
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv

load_dotenv()

pytestmark = pytest.mark.parametrize('link', [
    'https://stepik.org/lesson/236895/step/1',
    'https://stepik.org/lesson/236896/step/1',
    'https://stepik.org/lesson/236897/step/1',
    'https://stepik.org/lesson/236898/step/1',
    'https://stepik.org/lesson/236899/step/1',
    'https://stepik.org/lesson/236903/step/1',
    'https://stepik.org/lesson/236904/step/1',
    'https://stepik.org/lesson/236905/step/1'
    ])


def test_authorization(browser, link):
    
    browser.get(link)

    # Authorization
    WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.ember-view.navbar__auth.navbar__auth_login.st-link.st-link_style_button'))).click()
    WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.ID, 'id_login_email'))).send_keys(os.getenv('LOGIN'))
    WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.ID, 'id_login_password'))).send_keys(os.getenv('PASSWORD'))
    browser.find_element(By.CSS_SELECTOR, '.sign-form__btn.button_with-loader ').click()

    # Checks if the test needed to be restarted 
    try:
        WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.again-btn.white'))).click()
    except TimeoutException:

        answer = math.log(int(time.time()))

        WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.ember-text-area.ember-view.textarea.string-quiz__textarea'))).send_keys(answer)
        
        WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.submit-submission'))).click()
        # time.sleep(5)
        # browser.find_element(By.CSS_SELECTOR, '.submit-submission').click()

        result_text = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH, '//p[@class="smart-hints__hint"]')))
        # time.sleep(5)
        # result_text = browser.find_element(By.XPATH, '//p[@class="smart-hints__hint"]')
        result_text_actual = result_text.text
        result_text_expected = 'Correct!'

        assert result_text_expected == result_text_actual, f"Expected text is '{result_text_expected}', but it is '{result_text_actual}'"
