from selenium.webdriver.common.by import By


def xpath_selector(value: str):
    return By.XPATH, value


def css_selector(value: str):
    return By.CSS_SELECTOR, value


def id_selector(value: str):
    return By.ID, value


def text_selector(text: str, node="*"):
    return xpath_selector(
        f"//{node}[contains(text(), '{text}') or contains(. , '{text}')]"
    )


def tag_selector(value: str):
    return By.TAG_NAME, value
