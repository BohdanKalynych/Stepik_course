import math
from selenium import webdriver
import time
from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/math.html"
browser = webdriver.Chrome()
browser.get(link)

x_element = browser.find_element(By.CSS_SELECTOR, '#input_value')
x = x_element.text
y = calc(x)

text_field = browser.find_element(By.CSS_SELECTOR, '.form-control')
text_field.send_keys(y)

robot_checkbox = browser.find_element(By.CSS_SELECTOR, '#robotCheckbox')
robot_checkbox.click()

robots_rule_radiobutton = browser.find_element(By.CSS_SELECTOR, '#robotsRule')
robots_rule_radiobutton.click()

submit_button = browser.find_element(By.CSS_SELECTOR, '.btn-default')
submit_button.click()


