from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = 'http://suninjuly.github.io/execute_script.html'
browser = webdriver.Chrome()
browser.get(link)

x = int(browser.find_element(By.ID, "input_value").text)
answer = str(math.log(abs(12*math.sin(int(x)))))
input_answer = browser.find_element(By.TAG_NAME, "input")
input_answer.send_keys(answer)

move_1 = browser.find_element(By.ID, "robotCheckbox")
move_2 = browser.find_element(By.ID, "robotsRule")
end = browser.find_element(By.TAG_NAME, "button")
browser.execute_script("return arguments[0].scrollIntoView(true);", move_1)
move_1.click()
move_2.click()
end.click()
time.sleep(5)