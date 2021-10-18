from selenium import webdriver
import time, math

try: 
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    
    box_gold = browser.find_element_by_id("treasure")
    value_box = box_gold.get_attribute("valuex")

    # Ваш код, который считывает значение Х, высчитывает по формуле и заполняет поля и чеки.

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text


    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))


    y = calc(x)

    
    input_ans = browser.find_element_by_id("answer")
    input_ans.send_keys(y)

    checkbox_key = browser.find_element_by_id("robotCheckbox")
    checkbox_key.click()

    radiobutton_key = browser.find_element_by_id("robotsRule")
    radiobutton_key.click()

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(5)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()