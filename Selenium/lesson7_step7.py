from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = 'http://suninjuly.github.io/get_attribute.html'
browser = webdriver.Chrome()
browser.get(link)

element = browser.find_element(By.TAG_NAME, "img")
value = element.get_attribute("valuex")
answer = str(math.log(abs(12*math.sin(int(value)))))

input_answer = browser.find_element(By.TAG_NAME, "input")
input_answer.send_keys(answer)
move_1 = browser.find_element(By.ID, 'robotCheckbox')
move_1.click()
move_2 = browser.find_element(By.ID, "robotsRule")
move_2.click()
end = browser.find_element(By.TAG_NAME, "button")
end.click()
time.sleep(3)