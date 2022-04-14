import time
import pytest

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_button(browser):
    browser.get(link)
    time.sleep(1)
    add_to_basket = browser.find_element_by_class_name("btn-add-to-basket").tag_name
    assert add_to_basket == "button", f"Кнопка {add_to_basket} не существует"
