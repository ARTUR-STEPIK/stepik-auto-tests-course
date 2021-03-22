from selenium import webdriver
from selenium.webdriver.support.ui import Select
import math
import time
#функцию calc(), которая рассчитает и вернет вам значение функции, которое нужно ввести в текстовое поле
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
  
try: 
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
#считываем текст со страницы и вносим в переменную
    x_element = browser.find_element_by_css_selector("#input_value")
#считаем
    x = x_element.text
    y = calc(x)
#заносим данные в строку
    input1 = browser.find_element_by_css_selector("#answer")
    input1.send_keys(y)
#проскроллим вниз до кнопки
    button = browser.find_element_by_css_selector(".btn")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
#Выбираем чекбокс
    option1 = browser.find_element_by_css_selector("#robotCheckbox")
    option1.click()
#Выбираем радиобатон
    option2 = browser.find_element_by_css_selector("#robotsRule")
    option2.click()

# Отправляем заполненную форму
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
