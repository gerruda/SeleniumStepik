import time

from helper.driver import web_driver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import math


browser = web_driver().driver_init()
link = "https://suninjuly.github.io/math.html"
link2 = "http://suninjuly.github.io/registration2.html"


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


def test(link):
    try:
        browser.get(link)

        x_text = browser.find_element(By.ID, 'input_value').text
        y =calc(x_text)
        y_input = browser.find_element(By.ID, 'answer')
        y_input.send_keys(f'{y}')
        chekbox = browser.find_element(By.XPATH, '//label[@for="robotCheckbox"]')
        chekbox.click()
        chekbox2 = browser.find_element(By.XPATH, '//label[@for="robotsRule"]').click()
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
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
