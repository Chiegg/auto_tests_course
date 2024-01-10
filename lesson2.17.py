from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:

  link="http://suninjuly.github.io/get_attribute.html"
  browser=webdriver.Chrome()
  browser.get(link)

  x_element = browser.find_element(By.ID, "treasure")
  xx_element=x_element.get_attribute("valuex")
  x = xx_element
  y = calc(x)

  input1 = browser.find_element(By.CSS_SELECTOR, "input#answer")
  input1.send_keys(y)

  checkbox1=browser.find_element(By.CSS_SELECTOR, "input#robotCheckbox")
  checkbox1.click()

  radiobuttom1=browser.find_element(By.CSS_SELECTOR, "input#robotsRule")
  radiobuttom1.click()

  buttom1=browser.find_element(By.CSS_SELECTOR, "button.btn.btn-default")
  buttom1.click()

  time.sleep(1)


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()




  
