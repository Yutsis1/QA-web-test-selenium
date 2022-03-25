from typing import List

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from elements import BaseElement
from elements.selectors import text_selector


class BaseList(BaseElement):

    def __init__(self, driver: WebDriver, locator, name=None):
        super().__init__(driver, locator, name)

    def get_all_li(self) -> List[WebElement]:
        elem = self.element if self.element else self.find_element()  # type: WebElement
        return elem.find_elements_by_tag_name("li")

    def get_li(self, text):
        elem = self.element if self.element else self.find_element()  # type: WebElement
        by, xpath = text_selector(
            text=text,
            node="li")
        return elem.find_element(
            by, xpath
        )

    def get_div_from_li(self, text: str) -> WebElement:
        return self.get_li(text).find_element_by_xpath(f"//div[contains(., '{text}')]")

    def get_p_from_li(self, text: str) -> WebElement:
        return self.get_li(text).find_element_by_xpath(f"//p[contains(., '{text}')]")
