import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    link = "http://suninjuly.github.io/alert_accept.html"

    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.TAG_NAME, 'button').click()
    time.sleep(2)

    alert_wind = browser.switch_to.alert
    time.sleep(2)
    alert_wind.accept()

    x = int(browser.find_element(By.ID, 'input_value').text)
    answer = math.log(abs(12 * math.sin(x)))   # ln(abs(12*sin(x)))

    answer_field = browser.find_element(By.ID, 'answer')
    answer_field.send_keys(answer)

    browser.find_element(By.TAG_NAME, 'button').click()

finally:
    time.sleep(10)
    browser.close()