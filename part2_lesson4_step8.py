from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from math import log,sin

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    price = WebDriverWait(browser,12).until(EC.text_to_be_present_in_element((By.ID,"price"),"$100"))

    book_button = browser.find_element(By.CSS_SELECTOR, "#book")
    book_button.click()

    x = int(browser.find_element(By.CSS_SELECTOR, '#input_value').text)
    x_solved = str(log(abs(12*sin(x))))

    input_field = browser.find_element(By.CSS_SELECTOR, '#answer')
    input_field.send_keys(x_solved)

    submit = browser.find_element(By.XPATH, "//button[@type='submit']")
    submit.click()

finally:
    time.sleep(5)
    browser.quit()


