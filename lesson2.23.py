from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math
def calc(sum):
  return str(sum)

try:

  link="https://suninjuly.github.io/selects2.html"
  browser=webdriver.Chrome()
  browser.get(link)

  x_element = browser.find_element(By.ID, "num1")
  y_element = browser.find_element(By.ID, "num2")
  x=x_element.text
  y=y_element.text
  sum=int(x)+int(y)

  browser.find_element(By.TAG_NAME, "select").click()
  select = Select(browser.find_element(By.TAG_NAME, "select"))
  select.select_by_value(str(sum))

  buttom1=browser.find_element(By.CSS_SELECTOR, "button.btn.btn-default")
  buttom1.click()


  



  time.sleep(1)


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()




  
