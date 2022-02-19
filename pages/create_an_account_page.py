from pages.base_page import BasePage
from pages.locators import CreateAnAccountPageLocators

class CreateAnAccountPage(BasePage):
    """
    Create an account Page Object
    """
    def choose_gender(self, gender):
        """
        Clicks Mr if gender is male and Mrs otherwise
        """
        if gender == "male":
            # Choose Mr
            self.driver.find_element(*CreateAnAccountPageLocators.GENDER_MALE).click()
        else:
            # Choose Mrs
            self.driver.find_element(*CreateAnAccountPageLocators.GENDER_FEMALE).click()

    def enter_name(self, name):
        pass

    def enter_last_name(self, last_name):
        """
        Enters last name
        """
        el = self.driver.find_element(*CreateAnAccountPageLocators.LAST_NAME)
        el.send_keys(last_name)

    def enter_password(self, password):
        """
        Enters password
        """
        # Znajdź pole
        password_input = self.driver.find_element(*CreateAnAccountPageLocators.PASSWORD)
        # Wpisz w to pole podane hasło
        password_input.send_keys(password)

    def get_email(self):
        """
        Returns e-mail entered in an input below Last Name
        """
        el = self.driver.find_element(*CreateAnAccountPageLocators.EMAIL)
        return el.get_attribute("value")

    def _verify_page(self):
        """
        Verifies Create an Account Page
        """
        pass
