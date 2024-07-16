import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


try: 
    link = "http://suninjuly.github.io/file_input.html"

    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.XPATH, '//input[@name="firstname"]').send_keys('Name')
    browser.find_element(By.XPATH, '//input[@name="lastname"]').send_keys('Surname')
    browser.find_element(By.XPATH, '//input[@name="email"]').send_keys('name@mail.ru')

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'test_lesson_2_2_step8.txt')
    
    browser.find_element(By.ID, 'file').send_keys(file_path)

    browser.find_element(By.TAG_NAME, 'button').click()


finally:
    time.sleep(10)
    browser.close()