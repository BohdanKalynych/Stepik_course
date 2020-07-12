from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = int(browser.find_element(By.CSS_SELECTOR, '#num1').text)
    num2 = int(browser.find_element(By.CSS_SELECTOR, '#num2').text)
    num_sum = num1 + num2
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_visible_text(str(num_sum))
    submit = browser.find_element(By.CSS_SELECTOR, '.btn')
    submit.click()


finally:
    time.sleep(10)
    browser.quit()