from playwright.sync_api import expect


class Registration:
    def __init__(self, page):
        self.page = page

    def registering_form(self, name, family, uid, store_title, address, postalcode, role_id, store_phone):
        # self.click_name_input =
        self.page.get_by_placeholder("نام", exact=True).click()
        # self.fill_name_input =
        self.page.get_by_placeholder("نام", exact=True).fill(name)
        # self.click_family_input =
        self.page.get_by_placeholder("نام خانوادگی").click()
        # self.fill_family_input =
        self.page.get_by_placeholder("نام خانوادگی").fill(family)
        # self.click_uid_input =
        self.page.get_by_placeholder("کد ملی").click()
        # self.fill_uid_input =
        self.page.get_by_placeholder("کد ملی").fill(uid)
        # self.click_store_title_input =
        self.page.get_by_placeholder("نام فروشگاه").click()
        # self.fill_uid_input =
        self.page.get_by_placeholder("نام فروشگاه").fill(store_title)
        # self.click_store_type_dropdown =
        self.page.get_by_role("button", name="یک مورد را انتخاب کنید.").click()
        # self.click_store_type_name =
        self.page.get_by_role("option", name="سوپرمارکت").click()
        # self.click_address_input =
        self.page.get_by_placeholder("آدرس فروشگاه").click()
        # self.fill_address_input =
        self.page.get_by_placeholder("آدرس فروشگاه").fill(address)
        # self.click_postal_code_input =
        self.page.get_by_placeholder("کد پستی").click()
        # self.fill_postal_code_input =
        self.page.get_by_placeholder("کد پستی").fill(postalcode)
        # self.click_role_id_input =
        self.page.get_by_placeholder("کد نقش").click()
        # self.fill_role_id_input =
        self.page.get_by_placeholder("کد نقش").fill(role_id)
        # self.click_store_phone_input =
        self.page.get_by_placeholder("02100000000").click()
        # self.fill_store_phone_input =
        self.page.get_by_placeholder("02100000000").fill(store_phone)
        # self.click_terms_checkbox =
        self.page.get_by_role("checkbox").check()
        expect(self.page.get_by_role("checkbox")).to_be_checked()
        # self.click_confirm_register =
        self.page.get_by_role("button", name="ثبت فروشگاه").click()

    def should_see_form(self):
        locator = self.page.get_by_text("ثبت فروشگاه").first
        expect(locator).to_be_visible()
