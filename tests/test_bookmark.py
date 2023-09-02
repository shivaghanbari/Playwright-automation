from playwright.sync_api import Playwright
from models.login import LoginPage
from models.userprofile import Userprofile
from models.bookmark import Bookmark


def test_bookmark_product(playwright: Playwright):
    iphone_13 = playwright.devices['iPhone 13']
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(
        **iphone_13, record_video_dir="videos/")
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    page = context.new_page()
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.enter_phone(phone_number="09128164696")
    login_page.enter_otp(otp_code="8585")
    user_profile = Userprofile(page)
    bookmark_product = Bookmark(page)
    bookmark_product.find_product_by_search_bar()
    # user_profile.click_profile()

