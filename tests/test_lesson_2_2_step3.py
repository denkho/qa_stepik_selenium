import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

try:
    link = 'https://suninjuly.github.io/selects1.html'

    browser = webdriver.Chrome()
    browser.get(link)

    num1 = int(browser.find_element(By.ID, 'num1').text)
    num2 = int(browser.find_element(By.ID, 'num2').text)

    answer = num1 + num2

    select = Select(browser.find_element(By.ID, 'dropdown'))
    select.select_by_value(str(answer))

    browser.find_element(By.TAG_NAME, 'button').click()


finally:
    time.sleep(5)
    browser.close()