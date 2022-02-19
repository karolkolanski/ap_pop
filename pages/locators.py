from selenium.webdriver.common.by import By

class HomePageLocators():
    """
    Locators used on Home Page
    """
    SIGN_IN_LINK = (By.CLASS_NAME, "login")

class AuthenticationPageLocators():
    """
    Locators used on Authentication Page
    """
    CREATE_AN_ACCOUNT_EMAIL = (By.ID, "email_create")