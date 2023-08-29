
class StoreProfile:
    def __init__(self, page):
        self.page = page

    # this function redirect user to store page
    def click_my_stores(self):
        store_path = ".profile-body-items_profile-body-items__2MEMk > div:nth-child(2) > .MuiSvgIcon-root"
        self.page.locator(store_path).first.click()
        store_title = self.page.get_by_text("شیوا فروشگاه")
        store_title.is_visible()

    # this function check if an address is checked or not!
    def check_delivery_address(self):
        address_one = self.page.get_by_label("دریان نو")
        address_two = self.page.get_by_label("ظفر")

        # check that if a delivery address is checked or not to click on it
        is_checked_toggle = address_one.is_checked()

        if not is_checked_toggle:
            address_one.check()
        else:
            address_two.check()

    # this function changes delivery address to another one based on check delivery address
    def change_delivery_address(self):

        self.page.get_by_role("button", name="تایید آدرس تحویل", exact=True).click()

    # click on menu to open button sheet
    def click_menu_button(self):
        menu_button_path = ("#__next > div > div > div > div > div"
                            ".profile_profile__3AU7l.desktop-layout"
                            "_mobile-view__19WQP.is-mobile > div >"
                            " div.stores_content__wEl54 > div > div.edi"
                            "t-store-items_edit-stores-items__3_GWp > div.edit-store-items_store-title__Tk97m > svg")
        self.page.locator(menu_button_path).first.click()

    # this function add a new delivery address into user's store list
    def add_new_delivery_address(self, address_name):

        self.click_menu_button()
        self.page.get_by_text("افزودن آدرس تحویل (انبار)").click()
        self.page.get_by_role("textbox").click()
        self.page.get_by_role("textbox").fill(address_name)
        self.page.get_by_role("button", name="ثبت آدرس", exact=True).click()
        self.page.get_by_text("لیست فروشگاه‌ها").is_visible()

        # check if new delivery address is added or not and if it didn't refresh page to show it
        new_address_visibility = self.page.get_by_label("میدان ونک").first.is_visible()
        if new_address_visibility is False:
            self.page.reload()

    def remove_delivery_address(self):
        self.click_menu_button()
        self.page.get_by_text("ویرایش اطلاعات فروشگاه").click()

        trash_icon = (
            "#__next > div > div > div > div > div.profile_profile__3AU7l.desktop-layout_mobile-view__19WQP.is"
            "-mobile > div > div > div.auth-base_content__IqeJw.edit-store_content__3YnFC > "
            "div.add-delivery-address_add-delivery-address-container__2EWX1 > div:nth-child(3) > div > "
            "div.textarea_textarea-container__2qWHn > div > svg")
        finding_trash_icon = self.page.locator(trash_icon)
        finding_trash_icon.scroll_into_view_if_needed()
        finding_trash_icon.click()
        self.page.get_by_role("button", name="بله، حذف شود.").click()
        self.page.get_by_role("button", name="ذخیره").click()
