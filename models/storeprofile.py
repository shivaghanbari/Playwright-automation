from playwright.sync_api import expect


class StoreProfile:
    def __init__(self, page):
        self.page = page

    def click_store(self):
        store_path = ".profile-body-items_profile-body-items__2MEMk > div:nth-child(2) > .MuiSvgIcon-root"
        self.page.locator(store_path).first.click()
        store_title = self.page.get_by_text("فروشگاه‌های من")
        expect(store_title).to_be_visible()

    def change_store_address(self):
        address_one = self.page.get_by_label("دریان نو")
        address_two = self.page.get_by_label("ظفر")

        is_checked_toggle = address_one.is_checked()
        if not is_checked_toggle:
            address_one.check()

        address_two.check()

        self.page.get_by_role("button", name="تایید آدرس تحویل", exact=True).click()
