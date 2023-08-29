from playwright.sync_api import Playwright, expect
from models.login import LoginPage
from models.basket import BasketPage
from models.order import OrderPage

def test_order(playwright: Playwright):   
    iphone_13 = playwright.devices['iPhone 13']
    browser = playwright.webkit.launch(headless=False)
    context = browser.new_context(
        **iphone_13, record_video_dir="videos/")
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    page = context.new_page()
    login_page = LoginPage(page)
    basket_page = BasketPage(page)
    order_page = OrderPage(page)
    login_page.navigate()
    login_page.enter_phone(phone_number="09124785819")
    login_page.enter_otp(otp_code="8585")
    login_page.should_see_home()
    basket_page.click_basket()
    expect(page).to_have_title("سبد خرید")
    if basket_page.basket_has_items():
        basket_page.empty_basket()
    else:
        print("Basket was already empty.")
    basket_page.add_to_basket()
    basket_page.click_basket()
    basket_page.submit_basket()
    order_page.confirm_order()
    order_page.click_order_list()
    order_page.cancel_order()