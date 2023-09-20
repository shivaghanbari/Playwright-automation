import time
from playwright.sync_api import expect


class LoginPage:
    def __init__(self, page):
        self.page = page

    # Navigating to login page
    def navigate_to_login(self):
        self.page.get_by_role("link", name="Log in").click()

    def enter_email_username(self, email_username):
        # self.click_email_input =
        self.page.get_by_text("Username or Email").click()
        # self.enter_email =
        self.page.get_by_text("Username or Email").fill(email_username)

    def enter_password(self, password):
        # self.click_password_input =
        self.page.get_by_label("Password Forgot?").click()
        # self.enter_password =
        self.page.get_by_label("Password Forgot?").fill(password)

    def sign_in_button(self):
        self.page.get_by_role("button", name="Sign In", exact=True).click()
        time.sleep(2)

    def wrong_password(self):
        wrong_password_message = self.page.get_by_role("heading", name="We couldn’t find an account matching the "
                                                                       "username and password you entered. Please "
                                                                       "check your username and password and try "
                                                                       "again.")
        return wrong_password_message.is_visible()

    def forget_password(self):
        self.page.get_by_role("link", name="Forgot?").click()
        reset_button = self.page.get_by_role("button", name="Send Reset Instructions", exact=True)
        expect(reset_button).to_be_enabled()

    def enter_reset_email(self, reset_email):
        reset_button = self.page.get_by_role("button", name="Send Reset Instructions", exact=True)
        self.page.locator("#email").fill(reset_email)
        reset_button.click()

    def page_is_loaded(self):
        load_page = self.page.get_by_role("link", name="Discover")
        expect(load_page).to_be_visible()
