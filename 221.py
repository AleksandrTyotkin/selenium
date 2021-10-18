from selenium import webdriver
import time, math
from selenium.webdriver.support.ui import Select

try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    element = browser.find_element_by_id("num1") #получаем элемент из формы сайта
    str_num1 = element.get_attribute("textContent")

    element = browser.find_element_by_id("num2") #получаем элемент из формы сайта
    str_num2 = element.get_attribute("textContent")

    str_num1 = int(str_num1)
    str_num2 = int(str_num2)
    str_sum = str_num1 + str_num2
    str_sum = str(str_sum)

    #time.sleep(2)

    print(str_sum)

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(str_sum) # ищем элемент с текстом "Python"

    button = browser.find_element_by_css_selector("button.btn")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()