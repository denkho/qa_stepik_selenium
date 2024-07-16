import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    link = "http://suninjuly.github.io/execute_script.html"

    browser = webdriver.Chrome()
    browser.get(link)

    x = int(browser.find_element(By.ID, 'input_value').text)
    answer = math.log(abs(12 * math.sin(x)))   # ln(abs(12*sin(x)))

    button = browser.find_element(By.TAG_NAME, 'button')

    answer_field = browser.find_element(By.ID, 'answer')
    answer_field.send_keys(answer)
    browser.execute_script("return arguments[0].scrollIntoView(true);", answer_field)

    browser.find_element(By.ID, 'robotCheckbox').click()
    browser.find_element(By.ID, 'robotsRule').click()

    
    button.click()

finally:
    time.sleep(5)
    browser.close()