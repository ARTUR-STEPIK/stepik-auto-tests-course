from selenium import webdriver
from selenium.webdriver.support.ui import Select
import math
import time
#функцию calc(), которая рассчитает и вернет вам значение функции, которое нужно ввести в текстовое поле
def calc(x, y):
    return x + y
  
try: 
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)
#считываем текст со страницы и вносим в переменную
    x_element = browser.find_element_by_css_selector("#num1")
    y_element = browser.find_element_by_css_selector("#num2")
#заносим текстовые значения в переменные и конвертируем в числовой формат
    x = int(x_element.text)
    y = int(y_element.text)
    z = calc(x, y)
#конвертируем в строчное значение
    z = str(z)
    select = Select(browser.find_element_by_css_selector("#dropdown"))
    select.select_by_value(z)

 # Отправляем заполненную форму
    button = browser.find_element_by_css_selector(".btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
