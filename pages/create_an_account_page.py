from selenium.webdriver.support.select import Select

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

    def choose_birthdate(self, date):
        """
        Chooses Customer birthdate in YYYY-MM-DD format
        """
        # date = "1980-02-30"
        date_splitted = date.split("-")
        # date_splitted = ["1980", "02", "30"]
        year = date_splitted[0]    # "1980"
        month = str(int(date_splitted[1]))   # "02" => "2"
        day = date_splitted[2]     # "30"
        # Tworzymy instancję klasy Select
        # Ta klasa przyjmuje w inicjalizatorze WebElement
        # Służy do obsługi list wybieralnych
        # vide "Selenium ściąga" str. 8
        day_select = Select(self.driver.find_element(*CreateAnAccountPageLocators.BIRTHDATE_DAY))
        day_select.select_by_value(day)
        month_select = Select(self.driver.find_element(*CreateAnAccountPageLocators.BIRTHDATE_MONTH))
        month_select.select_by_value(month)
        year_select = Select(self.driver.find_element(*CreateAnAccountPageLocators.BIRTHDATE_YEAR))
        year_select.select_by_value(year)


    def get_email(self):
        """
        Returns e-mail entered in an input below Last Name
        """
        el = self.driver.find_element(*CreateAnAccountPageLocators.EMAIL)
        return el.get_attribute("value")

    def get_first_name(self):
        """
        Returns Address First Name
        """
        el = self.driver.find_element(*CreateAnAccountPageLocators.ADDRESS_FIRST_NAME)
        # Przewinięcie do elementu
        el.location_once_scrolled_into_view
        return el.get_attribute("value")

    def get_last_name(self):
        """
        Returns Address Last Name
        """
        el = self.driver.find_element(*CreateAnAccountPageLocators.ADDRESS_LAST_NAME)
        return el.get_attribute("value")


    def _verify_page(self):
        """
        Verifies Create an Account Page
        """
        pass
