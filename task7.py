import select
import time

from helper.driver import web_driver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import math
from selenium.webdriver.support.ui import Select



browser = web_driver().driver_init()
link = "http://suninjuly.github.io/execute_script.html"

# select.select_by_visible_text("text") и select.select_by_index(index)

def calc(x):
  return str(math.log(abs(12*math.sin(x))))


def test(link):
    try:
        browser.get(link)
        x = browser.find_element(By.ID, 'input_value').text
        y = calc(int(x))
        inp = browser.find_element(By.ID, "answer")
        browser.execute_script("return arguments[0].scrollIntoView(true);", inp)
        inp.send_keys(y)
        chekbox = browser.find_element(By.XPATH, '//label[@for="robotCheckbox"]')
        browser.execute_script("return arguments[0].scrollIntoView(true);", chekbox)
        chekbox.click()
        chekbox2 = browser.find_element(By.XPATH, '//label[@for="robotsRule"]')
        browser.execute_script("return arguments[0].scrollIntoView(true);", chekbox2)
        chekbox2.click()
        button = browser.find_element_by_tag_name("button")
        browser.execute_script("return arguments[0].scrollIntoView(true);", button)
        button.click()


    finally:
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(10)


if __name__ == "__main__":
    try:
        test(link)

    finally:
        # закрываем браузер после всех манипуляций
        browser.quit()
