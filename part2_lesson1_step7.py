import math
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
#adding some comments for new commit


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.CSS_SELECTOR, '#treasure').get_attribute("valuex")
    y = calc(x_element)

    text_field = browser.find_element(By.CSS_SELECTOR, '#answer')
    text_field.send_keys(y)

    robot_checkbox = browser.find_element(By.CSS_SELECTOR, '#robotCheckbox')
    robot_checkbox.click()

    robots_rule_radiobutton = browser.find_element(By.CSS_SELECTOR, '#robotsRule')
    robots_rule_radiobutton.click()

    submit_button = browser.find_element(By.CSS_SELECTOR, '.btn-default')
    submit_button.click()

finally:
    time.sleep(10)




