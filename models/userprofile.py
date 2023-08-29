from playwright.sync_api import expect
import time


class Userprofile:
    def __init__(self, page):
        self.page = page

    def click_profile(self):
        self.page.get_by_role("button", name="پروفایل").click()

    # this function checks some points like page name and user has name and family
    def check_user_profile(self):
        profile_path = ("#__next > div > div > div > div >"
                        " div.profile-header_profile-header"
                        "__3_8oy.is-mobile > div.profile-header"
                        "_info__1Jb8s > div.profile-header_left__1N9vV > svg")
        self.page.locator(profile_path).click()
        user_profile_title = self.page.get_by_text("ویرایش پروفایل")
        expect(user_profile_title).to_be_visible()
        name = self.page.get_by_role("textbox").first.input_value()
        print("name = ", name)
        family = self.page.get_by_role("textbox").nth(1).input_value()
        print("family = ", family)
        phone_number = self.page.get_by_role("spinbutton")
        expect(phone_number).to_be_disabled()

    # this function checks if user does not have name or family, should get error
    def edit_user_profile(self, name):
        remove_icon = (
            "#__next > div > div > div > div > div.profile_profile__3AU7l.desktop-layout_mobile-view__19WQP.is"
            "-mobile > div > div.edit-profile-body_top__4wny4 > div:nth-child(1) > "
            "div.undefined.input_input-container__2Z9r1 > svg")
        self.page.locator(remove_icon).click()
        self.page.get_by_role("button", name="ویرایش", exact=True).click()
        self.page.get_by_role("button", name="ذخیره تغییرات", exact=True).click()
        show_toast_message = self.page.get_by_text("نام و نام خانوادگی اجباری می باشد.")
        time.sleep(2)
        is_visible_toast = show_toast_message.is_visible()
        print(is_visible_toast)
        self.page.get_by_role("textbox").first.click()
        self.page.get_by_role("textbox").first.fill(name)
        self.page.get_by_role("button", name="ویرایش", exact=True).click()
        self.page.get_by_role("button", name="ذخیره تغییرات", exact=True).click()
