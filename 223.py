from selenium import webdriver
import time, math, os

try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    str_first_name = "firstname"
    input_first_name = browser.find_element_by_name("firstname")
    input_first_name.send_keys(str_first_name)

    str_last_name = str("lastname")
    input_last_name = browser.find_element_by_name("lastname")
    input_last_name.send_keys(str_last_name)

    str_email = str("email")
    input_email = browser.find_element_by_name("email")
    input_email.send_keys(str_email)


    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'for_223.txt')           # добавляем к этому пути имя файла 
    element = browser.find_element_by_id("file")
    element.send_keys(file_path)


    #browser.execute_script("window.scrollBy(0, 100);")


    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(10)

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