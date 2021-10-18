from selenium import webdriver
import time, unittest


class TestVerf(unittest.TestCase):
    def test_one(self):
        try:
            browser = webdriver.Chrome()
            browser.get("http://suninjuly.github.io/registration1.html")
            browser.find_element_by_css_selector(".first_block .first").send_keys("Alex")
            browser.find_element_by_css_selector(".first_block .second").send_keys("Ivanov")
            browser.find_element_by_css_selector(".first_block .third").send_keys("email@mail.ru")
            browser.find_element_by_css_selector("button.btn").click()
            time.sleep(2)

            self.assertEqual(browser.find_element_by_tag_name("h1").text, "Congratulations! You have successfully registered!", "Test is broken!")

        finally:
            time.sleep(5)
            browser.quit()

    def test_two(self):
        try:
            browser = webdriver.Chrome()
            browser.get("http://suninjuly.github.io/registration2.html")
            browser.find_element_by_css_selector(".first_block .first").send_keys("Alex")
            browser.find_element_by_css_selector(".first_block .second").send_keys("Ivanov")
            browser.find_element_by_css_selector(".first_block .third").send_keys("email@mail.ru")
            browser.find_element_by_css_selector("button.btn").click()
            time.sleep(2)

            self.assertEqual(browser.find_element_by_tag_name("h1").text, "Congratulations! You have successfully registered!", "Test is broken!")

        finally:
            time.sleep(5)
            browser.quit()
if __name__ == "__main__":
    unittest.main()
