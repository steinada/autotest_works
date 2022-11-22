from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = 'https://suninjuly.github.io/math.html'
browser = webdriver.Chrome()
browser.get(link)


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


x = browser.find_element(By.ID, 'input_value').text
answer = calc(x)
fill_ans = browser.find_element(By.ID, "answer")
fill_ans.send_keys(answer)
move_1 = browser.find_element(By.CSS_SELECTOR, '[for="robotCheckbox"]')
move_1.click()
move_2 = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
move_2.click()
end = browser.find_element(By.TAG_NAME, "button")
end.click()
time.sleep(10)