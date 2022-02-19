from pages.base_page import BasePage
from pages.locators import HomePageLocators

class HomePage(BasePage):
    """
    Landing Page Object
    """
    def click_sign_in(self):
        """
        Clicks Sign In link
        """
        # Zlokalizuj Sign In
        el = self.driver.find_element(*HomePageLocators.SIGN_IN_LINK)
        # Kliknij
        el.click()

    def _verify_page(self):
        """
        Verifies Home Page
        """
        pass