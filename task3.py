import time
from helper.driver import web_driver
from selenium.webdriver.common.by import By

browser = web_driver().driver_init()
link = "http://suninjuly.github.io/huge_form.html"

try:
    browser.get(link)
    elements = browser.find_elements(By.XPATH, '//input[@type="text"]')
    for element in elements:
        element.send_keys("Мой ответ")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
finally:
# успеваем скопировать код за 30 секунд
    time.sleep(30)
# закрываем браузер после всех манипуляций
    browser.quit()
