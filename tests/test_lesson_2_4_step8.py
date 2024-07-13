import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    WebDriverWait(browser, 10).until(EC.text_to_be_present_in_element((By.ID, 'price'), '100'))
    browser.find_element(By.XPATH, '//button[@id="book"]').click()

    x = int(browser.find_element(By.ID, 'input_value').text)
    answer = math.log(abs(12 * math.sin(x)))   # ln(abs(12*sin(x)))

    browser.find_element(By.ID, 'answer').send_keys(answer)
    browser.find_element(By.XPATH, '//button[@id="solve"]').click()

finally:
    time.sleep(10)
    browser.close()