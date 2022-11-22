from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

link = 'http://suninjuly.github.io/file_input.html'
browser = webdriver.Chrome()
browser.get(link)

input_1 = browser.find_element(By.XPATH, "//input[1]")
input_1.send_keys("Nasty")
input_2 = browser.find_element(By.XPATH, "//input[2]")
input_2.send_keys("Youri")
input_3 = browser.find_element(By.XPATH, "//input[3]")
input_3.send_keys("w@o.w")
element = browser.find_element(By.ID, "file")

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'text.txt')
element.send_keys(file_path)
end = browser.find_element(By.TAG_NAME, "button")
end.click()

time.sleep(5)