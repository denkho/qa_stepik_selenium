import time
from selenium import webdriver

try:
    browser = webdriver.Chrome()
    browser.execute_script("document.title='Script executing';")
    browser.execute_script("alert('Robots at work!')")

finally:
    time.sleep(5)
    browser.close()