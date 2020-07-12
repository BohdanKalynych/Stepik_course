from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from math import log,sin

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/alert_accept.html")

    start_button = browser.find_element(By.CSS_SELECTOR, '.btn')
    start_button.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    x = int(browser.find_element(By.CSS_SELECTOR, '#input_value').text)
    x_solved = str(log(abs(12*sin(x))))

    input_field = browser.find_element(By.CSS_SELECTOR, '#answer')
    input_field.send_keys(x_solved)

    submit = browser.find_element(By.XPATH, "//button[@type='submit']")
    submit.click()

finally:
    time.sleep(5)
    browser.quit()


