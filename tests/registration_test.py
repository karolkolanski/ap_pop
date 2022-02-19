from tests.base_test import BaseTest
from time import sleep

class RegistrationTest(BaseTest):
    """
    Registration Tests
    """
    def test_no_name(self):
        home_page = self.home_page
        # 1. Kliknij Sign In
        home_page.click_sign_in()

        # Zatrzymaj na chwilę test na końcu, by zdążyć
        # zauważyć co się dzieje
        sleep(2)