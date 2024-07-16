import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv

load_dotenv()

def test_authorization(browser):
    link = "https://stepik.org/lesson/236895/step/1"
    browser.get(link)

    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, 'ember459'))).click()
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, 'id_login_email'))).send_keys(os.getenv('LOGIN'))
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, 'id_login_password'))).send_keys(os.getenv('PASSWORD'))
    browser.find_element(By.CSS_SELECTOR, '.sign-form__btn.button_with-loader ').click()
    

    # browser.find_element(By.ID, 'ember459').click()
    # browser.find_element(By.ID, 'id_login_email').send_keys(os.getenv('LOGIN'))
    # browser.find_element(By.ID, 'id_login_password').send_keys(os.getenv('PASSWORD'))

    time.sleep(5)
