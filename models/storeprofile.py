import time
import pyautogui
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
        else:
            address_two.check()

        self.page.get_by_role("button", name="تایید آدرس تحویل", exact=True).click()

    def add_store_detail(self, address_describe):
        menu_button = ("#__next > div > div > div > div > div"
                       ".profile_profile__3AU7l.desktop-layout"
                       "_mobile-view__19WQP.is-mobile > div >"
                       " div.stores_content__wEl54 > div > div.edi"
                       "t-store-items_edit-stores-items__3_GWp > div.edit-store-items_store-title__Tk97m > svg")
        self.page.locator(menu_button).first.click()
        self.page.get_by_text("افزودن آدرس تحویل (انبار)").click()
        time.sleep(5)
        page_title = self.page.get_by_text("آدرس تحویل", exact=True).is_visible()
        print(page_title)
        self.page.get_by_role("textbox").click()
        self.page.get_by_role("textbox").fill(address_describe)
        self.page.get_by_role("button", name="ثبت آدرس", exact=True).click()
        time.sleep(5)
        new_address_visibility = self.page.get_by_label("میدان ونک").first.is_visible()
        if new_address_visibility is False:
            self.page.reload()

        new_address_visibility = self.page.get_by_label("میدان ونک").first.is_visible()
        print(new_address_visibility)



