import random
import string

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from page_object import QuestionPage


class TestQuestions(object):

    @pytest.fixture
    def preparation_test(self):
        """
        Pytest fixture for check installation of webdriver,
        :return:
        """
        self.driver = webdriver.Chrome(
            service=Service(
                ChromeDriverManager().install()
            )
        )
        self.page = QuestionPage(self.driver)
        self.driver.get("http://localhost:8000/")
        yield
        self.driver.quit()
        self.driver.stop_client()

    def test_create_question(self, preparation_test):
        """
        Simple test scenario. Include next steps:
            1.Add new question
            2. Check the answer
        :param preparation_test: pytest fixture for prepare test
        :return:
        """
        rand_str = lambda n: ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(n))
        random_question = rand_str(5)
        random_answer = rand_str(5)

        self.page.add_question(random_question, random_answer)

        question_line = self.page.list_section.get_li(random_question)
        question_line.click()
        assert self.page.list_section.get_p_from_li(random_answer).is_displayed()

    def test_remove_questions(self, preparation_test):
        """
        Test for check reset questions field
        :param preparation_test: pytest fixture for prepare test
        :return:
        """
        self.page.remove_question_button.click()
        # better not use in this way, but on page present only one field with that info and this is the last step
        assert self.driver.find_element_by_xpath("//div[contains(., 'No questions yet :-(')]").is_displayed()

    def test_sort_questions(self, preparation_test):
        """
        Scenario for test sort function. Expect that sort will from A to Z
        :param preparation_test:
        :return:
        """
        self.page.remove_question_button.click()
        for letter in string.ascii_uppercase[::-1]:
            self.page.add_question(letter, letter)

        fresh_list = [elem.text for elem in self.page.list_section.get_all_li()]
        self.page.sort_question_button.click()
        assert fresh_list[::-1] == [elem.text for elem in self.page.list_section.get_all_li()]

