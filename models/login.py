class LoginPage:
    def __init__(self, page):
        self.page = page

    def navigate_to_login(self):
        self.page.get_by_role("link", name="Log in").click()

    def enter_email(self, email):
        # self.click_email_input =
        self.page.get_by_text("Username or Email").click()
        # self.enter_email =
        self.page.get_by_text("Username or Email").fill(email)

    def enter_password(self, password):
        # self.click_password_input =
        self.page.get_by_text("Password").click()
        # self.enter_password =
        self.page.get_by_text("Password").fill(password)
