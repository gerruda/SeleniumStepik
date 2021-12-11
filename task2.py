from selenium import webdriver
import time
import math
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import task1
link = "https://suninjuly.github.io/find_link_text"

try:
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get(link)
    textToFind = str(math.ceil(math.pow(math.pi, math.e)*10000))
    link = browser.find_element(By.XPATH, f'//a[text()="{textToFind}"]')
    link.click()
    task1.form_input(browser)


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
