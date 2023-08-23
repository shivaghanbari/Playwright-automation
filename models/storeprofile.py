import re
import time
from playwright.sync_api import expect


class StoreProfile:
    def __init__(self, page):
        self.page = page

    # this function redirect user to store page
    def click_store(self):
        store_path = ".profile-body-items_profile-body-items__2MEMk > div:nth-child(2) > .MuiSvgIcon-root"
        self.page.locator(store_path).first.click()
        store_title = self.page.get_by_text("فروشگاه‌های من")
        expect(store_title).to_be_visible()

    # this function changes store address
    def change_store_address(self):
        address_one = self.page.get_by_label("دریان نو")
        address_two = self.page.get_by_label("ظفر")

        # check that if a store address is checked or not to click on it
        is_checked_toggle = address_one.is_checked()

        if not is_checked_toggle:
            address_one.check()
        else:
            address_two.check()

        self.page.get_by_role("button", name="تایید آدرس تحویل", exact=True).click()

    def menu_button(self):
        menu_button = ("#__next > div > div > div > div > div"
                       ".profile_profile__3AU7l.desktop-layout"
                       "_mobile-view__19WQP.is-mobile > div >"
                       " div.stores_content__wEl54 > div > div.edi"
                       "t-store-items_edit-stores-items__3_GWp > div.edit-store-items_store-title__Tk97m > svg")
        self.page.locator(menu_button).first.click()

    # this function add a new store address into user's store list
    def add_delivery_address(self, address_describe):
        self.menu_button()
        self.page.get_by_text("افزودن آدرس تحویل (انبار)").click()
        time.sleep(5)
        page_title = self.page.get_by_text("آدرس تحویل", exact=True).is_visible()
        print(page_title)
        self.page.get_by_role("textbox").click()
        self.page.get_by_role("textbox").fill(address_describe)
        self.page.get_by_role("button", name="ثبت آدرس", exact=True).click()
        time.sleep(5)
        # check if new store address is added or not and if it didn't refresh page to show it
        new_address_visibility = self.page.get_by_label("میدان ونک").first.is_visible()
        if new_address_visibility is False:
            self.page.reload()

        new_address_visibility = self.page.get_by_label("میدان ونک").first.is_visible()
        print(new_address_visibility)

    def remove_delivery_address(self):
        self.menu_button()
        self.page.get_by_text("ویرایش اطلاعات فروشگاه").click()
        for i in range(6):
            self.page.mouse.wheel(0, 150)
            time.sleep(1)
            i += 1
        self.page.locator("div").filter(has_text=re.compile(r"^آدرس تحویل\*میدان ونک$")).locator("svg").click()
        self.page.get_by_role("button", name="بله، حذف شود.").click()
        time.sleep(5)
