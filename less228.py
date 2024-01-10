import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:

  link = "http://suninjuly.github.io/file_input.html"
  browser = webdriver.Chrome()
  browser.get(link)
  current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
  file_path = os.path.join(current_dir, "file.txt") 
  element = browser.find_element(By.ID, "file")
  element.send_keys(file_path)


  polya = browser.find_elements(By.CSS_SELECTOR, "input")
  for pole in polya:
        pole.send_keys("check")

  button = browser.find_element(By.CSS_SELECTOR, "button")
  button.click()


  






finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()




  
