from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = 'http://suninjuly.github.io/get_attribute.html'
    browser = webdriver.Chrome()
    browser.get(link)

    # Получаем значение элемента на сайте
    x_element = browser.find_element(By.CSS_SELECTOR, '#treasure')
    x_value = x_element.get_attribute('valuex')
    y = calc(x_value)
    
    # Вставляем полученный ранее элемент в поле для ввода
    input1 = browser.find_element(By.CSS_SELECTOR, '#answer')
    input1.send_keys(y)

    # Находим элемент чек бокса и отмечаем его
    option1 = browser.find_element(By.CSS_SELECTOR, '#robotCheckbox')
    option1.click()

    # Задержка перед выполнением следующей команды
    time.sleep(1)

    # Находим элемент радиокнопки и отмечаем
    option2 = browser.find_element(By.CSS_SELECTOR, '#robotsRule')
    option2.click()


    # Нажимаем на кнопку    
    button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    button.click()

    time.sleep(1)


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit() 