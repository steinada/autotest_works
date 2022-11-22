from selenium import webdriver
from selenium.webdriver.common.by import By

try:
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

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    browser.quit()