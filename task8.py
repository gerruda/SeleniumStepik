import select
import time

from helper.driver import web_driver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import math
from selenium.webdriver.support.ui import Select
import os


browser = web_driver().driver_init()
link = "http://suninjuly.github.io/file_input.html"

# import os
#
# current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
# file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла
# element.send_keys(file_path)
# file_path = os.path.join(current_dir, 'file.txt')



def calc(x):
  return str(math.log(abs(12*math.sin(x))))


def test(link):
    try:
        browser.get(link)
        fname = browser.find_element(By.XPATH, '//input[@name="firstname"]')
        fname.send_keys('First')
        lname = browser.find_element(By.XPATH, '//input[@name="lastname"]')
        lname.send_keys('Last')
        email = browser.find_element(By.XPATH, '//input[@name="email"]')
        email.send_keys('Last@first.com')
        current_dir = os.path.abspath(os.path.dirname(__file__))
        file_path = os.path.join(current_dir, '1.txt')
        send_file = browser.find_element(By.ID, "file")
        send_file.send_keys(file_path)
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
