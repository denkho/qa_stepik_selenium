import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestRegistraion(unittest.TestCase):
    def test_registration_one(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        browser.find_element(By.XPATH, "//label[text()='First name*']/following-sibling::input").send_keys('Mark')
        browser.find_element(By.XPATH, "//label[text()='Last name*']/following-sibling::input").send_keys('Swen')
        browser.find_element(By.XPATH, "//label[text()='Email*']/following-sibling::input").send_keys('mark@mail.ru')

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        welcome_test_expected = "Congratulations! You have successfully registered!"

        self.assertEqual(welcome_test_expected, welcome_text, 
                         f'Welcome test should be "{welcome_test_expected}", but it is "{welcome_text}"')


    def test_registration_two(self):
        link = "http://suninjuly.github.io/registration2.html"

        browser = webdriver.Chrome()
        browser.get(link)

        browser.find_element(By.XPATH, "//label[text()='First name*']/following-sibling::input").send_keys('Mark')
        browser.find_element(By.XPATH, "//label[text()='Last name*']/following-sibling::input").send_keys('Swen')
        browser.find_element(By.XPATH, "//label[text()='Email*']/following-sibling::input").send_keys('mark@mail.ru')

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        welcome_test_expected = "Congratulations! You have successfully registered!"

        self.assertEqual(welcome_test_expected, welcome_text, 
                         f'Welcome test should be "{welcome_test_expected}", but it is "{welcome_text}"')


if __name__ == "__main__":
    unittest.main()
