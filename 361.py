import time
import math
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.maximize_window()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('url_pre', ["236895", "236896","236897", "236898","236899", "236903","236904", "236905"])
class TestMath:
    def test_guest_should_see_match(self, browser, url_pre):
        link = f"https://stepik.org/lesson/{url_pre}/step/1"
        browser.get(link)
        time.sleep(2)
        answer = math.log(int(time.time()))
        time.sleep(2)
        browser.find_element_by_class_name("string-quiz__textarea").send_keys(str(answer))
        time.sleep(2)
        browser.find_element_by_class_name("submit-submission").click()
        time.sleep(2)
        assert browser.find_element_by_class_name("smart-hints__hint").text == "Correct!",  "Everything ok!"
        	


