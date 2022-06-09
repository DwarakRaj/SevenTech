import string
import random
import pytest
from Pages.assignment_page import Page


class TestLoginPage:

    @pytest.fixture(autouse=True)
    def classSetUp1(self, one_time_set_up):
        self.page = Page(one_time_set_up)

    def test_broken_images(self):
        self.page.assert_broken_images("http://the-internet.herokuapp.com/broken_images")

    def test_invalid_login(self):
        base_url = "http://the-internet.herokuapp.com/login"
        invalid_username = "test123@gmail.com"
        invalid_password = "123456"
        error_message = "Your username is invalid!"
        self.page.validate_invalid_login(base_url,invalid_username, invalid_password, error_message)

    def test_alphabets_entry(self):
        '''IT creates any random alphabet & enters in the number field & checks whether that alphabet is is entered
        or not & based on that making the case pass/ fail '''

        base_url = "http://the-internet.herokuapp.com/inputs"
        random_alphabet = random.choice(string.ascii_letters)
        print("alphabet to enter -", random_alphabet)
        self.page.enter_random_alphabet(base_url, random_alphabet)

    def test_sort_table(self):
        base_url = "http://the-internet.herokuapp.com/tables"
        self.page.sort_table_data(base_url)

    def test_successful_notification(self):
        base_url = "http://the-internet.herokuapp.com/notification_message_rendered"
        self.page.render_success_message(base_url, "Action successful")
