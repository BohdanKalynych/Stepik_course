from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import os


try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    first_name = browser.find_element(By.NAME, 'firstname')
    first_name.send_keys("firstname")

    last_name = browser.find_element(By.NAME, 'lastname')
    last_name.send_keys("lastname")

    email = browser.find_element(By.NAME, 'email')
    email.send_keys("email")

    file = browser.find_element(By.NAME, 'file')
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    file.send_keys(file_path)

    submit = browser.find_element(By.CSS_SELECTOR, '.btn')
    submit.click()

finally:
    time.sleep(5)
    browser.quit()
