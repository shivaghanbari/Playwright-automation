from playwright.sync_api import Playwright
from models.login import LoginPage
from models.navigate import Navigate
from utils.common_functions import CommonTools


# Steps
def test_login(playwright: Playwright):
    browser = playwright.webkit.launch(headless=False)
    context = browser.new_context(record_video_dir="videos/")
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    page = context.new_page()
    navigate_page = Navigate(page)
    navigate_page.navigate()
    common_tools = CommonTools(page)
    login_page = LoginPage(page)
    login_page.navigate_to_login()
    common_tools.check_page_is_loaded(page_title="Sign in to Dribbble")
    username_email = input("Enter Email or Username: ")
    login_page.enter_email_username(email_username=username_email)
    user_password = input("Enter Password,\nenter idk if you do not remember:\u00A0")
    if user_password == "idk":
        login_page.forget_password()
        reset_email = input("Enter reset email:\u00A0")
        login_page.enter_reset_email(reset_email=reset_email)
    else:
        login_page.enter_password(password=user_password)
        login_page.sign_in_button()
        login_page.page_is_loaded()
