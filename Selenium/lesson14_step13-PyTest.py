import unittest
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestRegistration(unittest.TestCase):
    def test_registration1(self):
        link = 'http://suninjuly.github.io/registration1.html'
        browser = webdriver.Chrome()
        browser.get(link)

        selectors = ['div.first_block .form-control.first',
                     'div.first_block .form-control.second', 'div.first_block .form-control.third']
        data = ['Anna', 'Robert', 'fl@ir.o']
        for i in range(3):
            new_input = browser.find_element(By.CSS_SELECTOR, selectors[i])
            new_input.send_keys(data[i])

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Failed registration")

    def test_registration2(self):
        link = 'http://suninjuly.github.io/registration2.html'
        browser = webdriver.Chrome()
        browser.get(link)

        selectors = ['div.first_block .form-control.first',
                     'div.first_block .form-control.second', 'div.first_block .form-control.third']
        data = ['Anna', 'Robert', 'fl@ir.o']
        for i in range(3):
            new_input = browser.find_element(By.CSS_SELECTOR, selectors[i])
            new_input.send_keys(data[i])

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Failed registration")


if __name__ == "__main__":
    pytest.main()
