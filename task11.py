import select
import time

from helper.driver import web_driver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import math
from selenium.webdriver.support.ui import Select
import os
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

browser = web_driver().driver_init()
link = "http://suninjuly.github.io/explicit_wait2.html"


def calc(x):
    return str(math.log(abs(12 * math.sin(x))))


def test(link):
    try:
        browser.get(link)
        price = WebDriverWait(browser, 12).until(
            EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        x_text = browser.find_element(By.XPATH, '//span[@id="input_value"]').text
        y = calc(int(x_text))
        answer = browser.find_element(By.XPATH, '//input[@id="answer"]')
        answer.send_keys(f'{y}')
        button = browser.find_element(By.ID, "solve")
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
