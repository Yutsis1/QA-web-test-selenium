from selenium.webdriver.remote.webdriver import WebDriver

from elements import BaseElement
from elements.base_button import BaseButton
from elements.base_input import BaseInput
from elements.base_list import BaseList
from elements.selectors import *


class QuestionPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

        # buttons
        self.create_question_button = BaseButton(
            self.driver,
            text_selector(
                "Create question",
                "button"
            )
        )
        self.sort_question_button = BaseButton(
            self.driver,
            text_selector(
                "Sort questions",
                "button"
            )
        )
        self.remove_question_button = BaseButton(
            self.driver,
            text_selector(
                "Remove questions",
                "button"
            )
        )

        # Inputs
        self.question_input = BaseInput(
            self.driver,
            id_selector("question")
        )
        self.answer_input = BaseInput(
            self.driver,
            id_selector("answer")
        )

        # list
        self.list_section = BaseList(
            self.driver,
            xpath_selector("//div[@class='card']")
        )

    def add_question(self,
                     question_text: str,
                     answer_test: str
                     ):
        self.question_input.send_text(question_text)
        self.answer_input.send_text(answer_test)
        self.create_question_button.click()
