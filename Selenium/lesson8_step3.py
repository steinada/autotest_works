from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

link = 'https://suninjuly.github.io/selects1.html'
browser = webdriver.Chrome()
browser.get(link)

num1 = browser.find_element(By.ID, "num1").text
num2 = browser.find_element(By.ID, "num2").text

select = Select(browser.find_element(By.TAG_NAME, "select"))
select.select_by_visible_text(str(int(num1)+int(num2)))
end = browser.find_element(By.TAG_NAME, "button")
end.click()
time.sleep(5)