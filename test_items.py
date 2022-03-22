import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_find_btn_add_basket_pass(browser):
    browser.get(link)
    time.sleep(5)
    browser.find_element_by_css_selector("button.btn-add-to-basket")
    assert browser.find_element_by_css_selector("button.btn-add-to-basket").text == "Ajouter au panier", \
                                                                                    "Test is broken!"
