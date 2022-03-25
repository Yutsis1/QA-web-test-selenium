from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class BaseElement:

    def __init__(self, driver: WebDriver, locator, name=None):
        self.driver = driver
        self.locator = locator
        self.name = name if name else "{}:{}".format(locator[0], locator[1])
        self.element = None

    def _wait_for(self, condition, exception_text: str, timeout=5):

        try:
            element = WebDriverWait(
                self.driver,
                timeout,
            ).until(
                condition((self.locator[0], self.locator[1]))
            )
            return element
        except TimeoutError:
            raise NoSuchElementException(exception_text)

    def find_element(self, timeout=5):
        return (self._wait_for(
            ec.presence_of_element_located,
            exception_text=f"{self.name} is not found",
            timeout=timeout
        ) if not self.element else self.element)

    def find_elements(self, timeout=5):
        return self._wait_for(
            ec.presence_of_all_elements_located,
            timeout=timeout,
            exception_text=f"No one {self.element} are found"
        )

    def wait_for_element_become_clickable(self, timeout=5):
        return self._wait_for(
            ec.element_to_be_clickable,
            timeout=timeout,
            exception_text=f"{self.element} is not clickable"
        )

    def wait_for_element_become_visible(self, timeout=5):
        return self._wait_for(
            ec.visibility_of_element_located,
            timeout=timeout,
            exception_text=f"{self.element} is not visible"
        )

    def click(self):
        element = self.find_element()
        # scroll to be in focus
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'})", element
        )
        element.click()
        return element

