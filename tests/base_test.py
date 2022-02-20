from pages.home_page import HomePage

from selenium import webdriver
import unittest

class BaseTest(unittest.TestCase):
    """
    Base class for each test
    """
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("http://automationpractice.com/")
        self.driver.implicitly_wait(10)
        # Stworzyć instancję klasy HomePage
        # Aby uzyskać dostęp do mechanizmów tej strony
        self.home_page = HomePage(self.driver)

    def tearDown(self):
        self.driver.quit()