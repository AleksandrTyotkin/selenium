from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time, math, os


try: 
	browser = webdriver.Chrome()
	browser.get("http://suninjuly.github.io/explicit_wait2.html")

	button = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))

	if button == True:
		btn = browser.find_element_by_id("book")
		btn.click()



	x_element = browser.find_element_by_id("input_value")
	x = x_element.text

	def calc(x):
		return str(math.log(abs(12*math.sin(int(x)))))


	y = calc(x)

	input_ans = browser.find_element_by_id("answer")
	input_ans.send_keys(y)
    
     
	browser.execute_script("window.scrollBy(0, 100);")


    # Отправляем заполненную форму
	button_1 = browser.find_element_by_id("solve")
	button_1.click()

	#assert "successful" in message.text
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(1000)
    # закрываем браузер после всех манипуляций
    browser.quit()