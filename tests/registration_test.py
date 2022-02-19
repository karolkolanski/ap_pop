from tests.base_test import BaseTest
from tests.test_data import TestData
from time import sleep

class RegistrationTest(BaseTest):
    """
    Registration Tests
    """
    def test_no_name(self):
        home_page = self.home_page
        # 1. Kliknij Sign In
        authentication_page = home_page.click_sign_in()
        # 2. Wpisz e-mail
        # 3. Kliknij przycisk „Create account”
        create_an_account_page = authentication_page.create_account_with_email(TestData.email)
        # 4. Wybierz płeć
        create_an_account_page.choose_gender(TestData.gender)

        # Zatrzymaj na chwilę test na końcu, by zdążyć
        # zauważyć co się dzieje
        sleep(3)