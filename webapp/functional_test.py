from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_poll_apps(self):
        # User Try to access to my poll apps
        self.browser.get('http://localhost:8000/poll/1/')

        # User notices the page title and header mention Poll&Choice
        self.assertIn('Poll&Choice', self.browser.title)

        # User


if __name__ == '__main__':
    unittest.main(warnings='ignore')
