from playwright.sync_api import expect


class LoginPage:
    def __init__(self, page):
        self.page = page

    def navigate(self):
        self.page.goto("https://dribbble.com/session/new")

    def enter_phone(self, phone_number):
        # self.click_phone_input =
        self.page.get_by_placeholder("09123456789").click()
        # self.enter_phone =
        self.page.get_by_placeholder("09123456789").fill(phone_number)
        # self.click_otp_btn =
        self.page.get_by_role("button", name="دریافت کد تایید").click()

    def enter_otp(self, otp_code):
        # self.click_otp_input = 
        self.page.get_by_role("spinbutton", name="Please enter OTP character 1").click()
        # self.enter_otp_code1 = 
        self.page.get_by_role("spinbutton", name="Please enter OTP character 1").fill(otp_code[0])
        # self.enter_otp_code2 = 
        self.page.get_by_role("spinbutton", name="Please enter OTP character 2").fill(otp_code[1])
        # self.enter_otp_code3 = 
        self.page.get_by_role("spinbutton", name="Please enter OTP character 3").fill(otp_code[2])
        # self.enter_otp_code4 = 
        self.page.get_by_role("spinbutton", name="Please enter OTP character 4").fill(otp_code[3])

    def should_see_home(self):
        locator = self.page.get_by_role("button", name="خانه")
        expect(locator).to_be_enabled()
