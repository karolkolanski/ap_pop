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
        # 5. Wpisz nazwisko
        create_an_account_page.enter_last_name(TestData.last_name)
        # 6. Sprawdź poprawność e-maila
        self.assertEqual(create_an_account_page.get_email(), TestData.email, "Mail differs from entered previously!")
        # 7. Wpisz hasło
        create_an_account_page.enter_password(TestData.password)
        # 8. Wybierz datę urodzenia
        create_an_account_page.choose_birthdate(TestData.birthdate)
        # 9. Sprawdź pole „First name”
        self.assertEqual(create_an_account_page.get_first_name(), "")
        # 10. Sprawdź pole „Last name”
        self.assertEqual(create_an_account_page.get_last_name(), TestData.last_name)



        # Zatrzymaj na chwilę test na końcu, by zdążyć
        # zauważyć co się dzieje
        sleep(3)