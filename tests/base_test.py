import unittest
from selenium import webdriver

class BaseTest(unittest.TestCase):
    """
    Base class for each test
    """
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get("http://automationpractice.com/")

    def tearDown(self):
        self.driver.quit()