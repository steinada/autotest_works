from selenium import webdriver
from selenium.webdriver.common.by import By
import math

link = 'http://suninjuly.github.io/redirect_accept.html'
browser = webdriver.Chrome()
browser.get(link)

button = browser.find_element(By.TAG_NAME, "button")
button.click()
new_window = browser.window_handles[1]
browser.switch_to.window(new_window)
num = int(browser.find_element(By.ID, "input_value").text)
result = str(math.log(abs(12*math.sin(num))))
input_1 = browser.find_element(By.ID, "answer")
input_1.send_keys(result)
submit = browser.find_element(By.TAG_NAME, "button")
submit.click()

print(browser.switch_to.alert.text)