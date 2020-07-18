from selenium import webdriver
import time
from selenium.webdriver.common.by import By

try:
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    first_name_field = browser.find_element(By.XPATH, "//label[text()='First name*']//following-sibling::input")
    first_name_field.send_keys("First_name")

    last_name_filed = browser.find_element(By.XPATH, "//label[text()='Last name*']//following-sibling::input")
    last_name_filed.send_keys("Last_name")

    email_field = browser.find_element(By.XPATH, "//label[text()='Email*']//following-sibling::input")
    email_field.send_keys("user_email")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    time.sleep(1)

    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()
