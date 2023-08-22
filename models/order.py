from playwright.sync_api import expect


class OrderPage:
    def __init__(self, page):
        self.page = page 

    def confirm_order(self):
        self.page.get_by_role("button", name="ثبت سفارش").click()

    def click_order_list(self):
        self.page.get_by_role("button", name="لیست سفارش‌ها").click()

    def cancel_order(self):
        self.page.get_by_role("button", name="لغو سفارش").first.click()
        expect(self.page.get_by_role("div", name="سفارش شما لغو گردید.")).to_be_visible()
