import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = 'https://suninjuly.github.io/math.html'

    browser = webdriver.Chrome()
    browser.get(link)

    x = int(browser.find_element(By.ID, 'input_value').text)
    browser.find_element(By.ID, 'answer').send_keys(calc(x))
    browser.find_element(By.CLASS_NAME, 'form-check-input').click()
    browser.find_element(By.ID,'robotsRule').click()
    
    browser.find_element(By.TAG_NAME, 'button').click()
    time.sleep(3)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
