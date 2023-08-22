from playwright.sync_api import Playwright
from models.login import LoginPage
from models.userprofile import Userprofile
from models.storeprofile import StoreProfile


def test_store_profile(playwright: Playwright):
    iphone_13 = playwright.devices['iPhone 13']
    browser = playwright.webkit.launch(headless=False)
    context = browser.new_context(
        **iphone_13, record_video_dir="videos/")
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    page = context.new_page()
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.enter_phone(phone_number="09128164696")
    login_page.enter_otp(otp_code="8585")
    user_profile = Userprofile(page)
    user_profile.click_profile()
    store_profile = StoreProfile(page)
    store_profile.click_store()
    store_profile.add_store_address(address_describe="میدان ونک")
    store_profile.change_store_address()


