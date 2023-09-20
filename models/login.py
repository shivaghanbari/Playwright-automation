import time
from playwright.sync_api import expect


class LoginPage:
    def __init__(self, page):
        self.page = page

    # Navigating to login page
    def navigate_to_login(self):
        self.page.get_by_role("link", name="Log in").click()

    # Clicks and fills the Username or Email input field
    def enter_email_username(self, email_username):
        self.page.get_by_text("Username or Email").click()
        self.page.get_by_text("Username or Email").fill(email_username)

    # Clicks and fills the Password input field
    def enter_password(self, password):
        self.page.get_by_label("Password Forgot?").click()
        self.page.get_by_label("Password Forgot?").fill(password)

    # Clicks the "Sign In" button
    def sign_in_button(self):
        self.page.get_by_role("button", name="Sign In", exact=True).click()
        time.sleep(2)

    # Checks if the "wrong password" message is visible
    def wrong_password(self):
        # Locates the "wrong password" message
        wrong_password_message = self.page.get_by_role("heading", name="We couldn’t find an account matching the "
                                                                       "username and password you entered. Please "
                                                                       "check your username and password and try "
                                                                       "again.")
        return wrong_password_message.is_visible()

    # Clicks the "Forgot?" link and checks if the reset button is enabled
    def forget_password(self):
        # Clicks the "Forgot?" link
        self.page.get_by_role("link", name="Forgot?").click()
        # Checks if the "Send Reset Instructions" button is enabled
        reset_button = self.page.get_by_role("button", name="Send Reset Instructions", exact=True)
        expect(reset_button).to_be_enabled()

    # Enters the reset email and clicks the "Send Reset Instructions" button
    def enter_reset_email(self, reset_email):
        # Locates the "Send Reset Instructions" button
        reset_button = self.page.get_by_role("button", name="Send Reset Instructions", exact=True)
        # Fills in the reset email
        self.page.locator("#email").fill(reset_email)
        # Clicks the "Send Reset Instructions" button
        reset_button.click()

    # Checks if the page is loaded by looking for the "Discover" link
    def page_is_loaded(self):
        # Locates the "Discover" link
        load_page = self.page.get_by_role("link", name="Discover")
        # Expects the "Discover" link to be visible
        expect(load_page).to_be_visible()
