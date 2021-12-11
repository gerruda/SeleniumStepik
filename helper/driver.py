from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class web_driver:
    def driver_init(self):
        return webdriver.Chrome(ChromeDriverManager().install())
