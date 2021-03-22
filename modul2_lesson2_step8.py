from selenium import webdriver
import time
import os

try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
#заполняем форму
    input1 = browser.find_element_by_name("firstname")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name("lastname")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_name("email")
    input3.send_keys("Smolensk@dd.rt")
# получаем путь к директории текущего исполняемого скрипта lesson2_7.py
    current_dir = os.path.abspath(os.path.dirname("/home/kuramshin/Downloads/AUTOTEST/Moduls/modul2_lesson2_step8.py"))
# имя файла, который будем загружать на сайт
    file_name = "file_example.txt"
# получаем путь к file_example.txt
    file_path = os.path.join(current_dir, file_name)
#кнопка отправки
    element = browser.find_element_by_css_selector('#file')
# отправляем файл
    element.send_keys(file_path)
# Отправляем заполненную форму
    button = browser.find_element_by_css_selector(".btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
