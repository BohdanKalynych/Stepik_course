from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import unittest


class UnitTestLike(unittest.TestCase):

    link1 = 'http://suninjuly.github.io/registration1.html'
    link2 = 'http://suninjuly.github.io/registration2.html'
    expected_text = "Congratulations! You have successfully registered!"

    def run_preconditions(self, link):
        self.browser = webdriver.Chrome()
        self.browser.get(link)
        self.__class__.first_name_field = self.browser.find_element(By.XPATH,
                                                                    "//label[text()='First name*']//following-sibling::input")
        self.__class__.last_name_filed = self.browser.find_element(By.XPATH,
                                                                    "//label[text()='Last name*']//following-sibling::input")
        self.__class__.email_field = self.browser.find_element(By.XPATH,
                                                                "//label[text()='Email*']//following-sibling::input")
        self.__class__.button = self.browser.find_element_by_css_selector("button.btn")

    def broswer_quit(self):
        time.sleep(2)
        self.browser.quit()

    def test_registration1(self):
        self.run_preconditions(self.link1)
        self.first_name_field.send_keys("First_name")
        self.last_name_filed.send_keys("Last_name")
        self.email_field.send_keys("user_email")
        self.button.click()

        welcome_text_el = self.browser.find_element_by_tag_name("h1")
        self.assertEqual(self.expected_text, welcome_text_el.text, "Registration is failed")

        self.broswer_quit()

    def test_registration2(self):
        self.run_preconditions(self.link2)
        self.first_name_field.send_keys("First_name")
        self.last_name_filed.send_keys("Last_name")
        self.email_field.send_keys("user_email")
        self.button.click()

        welcome_text_el = self.browser.find_element_by_tag_name("h1")
        self.assertEqual(self.expected_text, welcome_text_el.text, "Registration is failed")

        self.browser_quit()


if __name__ == "__main__":
    unittest.main()
