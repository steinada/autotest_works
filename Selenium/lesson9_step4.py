from selenium import webdriver
from selenium.webdriver.common.by import By
import math

link = 'http://suninjuly.github.io/alert_accept.html'
browser = webdriver.Chrome()
browser.get(link)

button = browser.find_element(By.TAG_NAME, "button")
button.click()
alert = browser.switch_to.alert
alert.accept()
num = int(browser.find_element(By.ID, "input_value").text)
result = str(math.log(abs(12*math.sin(int(num)))))
input_1 = browser.find_element(By.CLASS_NAME, "form-control")
input_1.send_keys(result)
sent = browser.find_element(By.TAG_NAME, "button")
sent.click()
alert_2 = browser.switch_to.alert
result_2 = alert_2.text
print(result_2)