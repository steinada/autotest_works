from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = 'http://suninjuly.github.io/registration1.html'
    browser = webdriver.Chrome()
    browser.get(link)

    # список селекторов для полей ввода
    selectors = ['.form-control[placeholder="Input your first name"]',
                 '.form-control[placeholder="Input your last name"]', '.form-control[placeholder="Input your email"]']
    # список данных для ввода
    data = ['Anna', 'Robert', 'fl@ir.o']
    # цикл для прохода по селекторам и соответствующим данным для ввода
    for i in range(3):
        new_input = browser.find_element(By.CSS_SELECTOR, selectors[i])
        new_input.send_keys(data[i])

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    time.sleep(1)

    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()