from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from math import log,sin


try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = int(browser.find_element(By.CSS_SELECTOR, '.nowrap#input_value').text)
    x_solved = str(log(abs(12*sin(x_element))))

    text_field = browser.find_element(By.CSS_SELECTOR, '#answer')
    browser.execute_script("return arguments[0].scrollIntoView(true);", text_field)
    text_field.send_keys(x_solved)

    robot_checkbox = browser.find_element(By.CSS_SELECTOR, '#robotcheckbox')
    robot_checkbox.click()

    robots_radio_button = browser.find_element(By.CSS_SELECTOR, '#robotsRule')
    robots_radio_button.click()

    submit_button = browser.find_element(By.CSS_SELECTOR, '.btn')
    submit_button.click()

finally:
    time.sleep(10)
    browser.quit()