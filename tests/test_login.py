import time
from playwright.sync_api import Playwright
from models.login import LoginPage
from models.navigate import Navigate


def test_login(playwright: Playwright):
    browser = playwright.webkit.launch(headless=False)
    context = browser.new_context(record_video_dir="videos/")
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    page = context.new_page()
    navigate_page = Navigate(page)
    navigate_page.navigate()
    login_page = LoginPage(page)
    login_page.navigate_to_login()
    user_email = input("Enter Email: ")
    user_password = input("Enter Password: ")
    login_page.enter_email(email=user_email)
    login_page.enter_password(password=user_password)
    time.sleep(5)

