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
    # we used a for loop to preview whole bookmark and un-bookmark scenario.
    for i in range(2):
        bookmark_product.set_bookmark(my_product="پوشک چسبی مای بیبی سری مهربان باپوست سایز0نرمال22عددی")
    # user_profile.click_profile()
