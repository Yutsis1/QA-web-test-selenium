from selenium.webdriver.chrome.webdriver import WebDriver

from elements import BaseElement


class BaseInput(BaseElement):
    def __init__(self, driver: WebDriver, locator, name=None):
        super().__init__(driver, locator, name)

    def send_text(self, text):
        self.find_element().send_keys(text)

    def clear(self):
        self.find_element().clear()