from tests.base_test import BaseTest

class RegistrationTest(BaseTest):
    """
    Registration Tests
    """
    def test_no_name(self):
        # 1. Kliknij Sign In
        self.home_page.click_sign_in()