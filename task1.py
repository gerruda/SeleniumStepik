import time
from selenium.webdriver.common.by import By
from helper.driver import web_driver


def form_input(browser):
    input1 = browser.find_element(By.XPATH, '//input[@name="first_name"]')
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.XPATH, '//input[@name="last_name"]')
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.XPATH, '//input[@class="form-control city"]')
    input3.send_keys("Smolensk")
    input4 = browser.find_element(By.XPATH, '//input[@id="country"]')
    input4.send_keys("Russia")
    button = browser.find_element(By.XPATH, '//button[@type="submit"]')
    button.click()
    time.sleep(30)
    browser.quit()


if __name__ == '__main__':
    link = "https://suninjuly.github.io/find_xpath_form"
    browser = web_driver().driver_init()
    browser.get(link)
    form_input(browser)
