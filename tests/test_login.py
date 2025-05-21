from playwright.sync_api import Playwright
from models.login import LoginPage
from models.navigate import Navigate
from utils.common_functions import CommonTools


# Steps
def test_login(playwright: Playwright):
    # Launch the browser
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context(record_video_dir="videos/")
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    page = context.new_page()

    # Initialize page objects
    navigate_page = Navigate(page)
    common_tools = CommonTools(page)
    login_page = LoginPage(page)

    # Navigate to the login page
    navigate_page.navigate()
    login_page.navigate_to_login()

    # Check if the login page is loaded
    common_tools.check_page_is_loaded(page_title="Sign in to Dribbble")

    # Prompt the user for email/username and password
    username_email = input("Enter Email or Username: ")
    login_page.enter_email_username(email_username=username_email)
    user_password = input("Enter Password,\nenter idk if you do not remember:\u00A0")

    if user_password == "idk":
        # Perform password reset flow
        login_page.forget_password()
        reset_email = input("Enter reset email:\u00A0")
        login_page.enter_reset_email(reset_email=reset_email)
    else:
        # Perform login with provided credentials
        login_page.enter_password(password=user_password)
        login_page.sign_in_button()

        # Check if the login was unsuccessful (wrong password)
        if login_page.wrong_password():
            retry_password = input("Enter correct password:\u00A0")
            login_page.enter_password(password=retry_password)
            login_page.sign_in_button()
        else:
            # Login successful, wait for the page to load
            login_page.page_is_loaded()

    # Cleanup: Close the browser context and stop tracing
    context.close()
