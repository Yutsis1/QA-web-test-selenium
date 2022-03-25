from selenium.webdriver.remote.webdriver import WebDriver

from elements import BaseElement


class BaseButton(BaseElement):
    def __init__(self, driver: WebDriver, locator, name=None):
        super().__init__(driver, locator, name)