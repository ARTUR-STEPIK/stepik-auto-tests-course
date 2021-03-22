from selenium import webdriver
import math
import time
#функцию calc(), которая рассчитает и вернет вам значение функции, которое нужно ввести в текстовое поле
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
  
try: 
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)
#считываем текст со страницы и вносим в переменную
    x_element = browser.find_element_by_css_selector("[valuex]").get_attribute("valuex")
    x = x_element.valuex
    y = calc(x)
    input1 = browser.find_element_by_css_selector("#answer")
    input1.send_keys(y)
#Выбираем чекбокс
    option1 = browser.find_element_by_css_selector("[for='robotCheckbox']")
    option1.click()
#Выбираем радиобатон
    option2 = browser.find_element_by_css_selector("#robotsRule.form-check-input")
    option2.click()

 # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
