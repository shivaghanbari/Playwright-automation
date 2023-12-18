# from playwright.sync_api import Playwright
# from models.login import LoginPage
# from models.register import Registration
# import random
#
#
# def generate_phone_number():
#     prefix = "09"
#
#     # number = prefix + str(random.randint(10, 99)) + str(random.randint(10000000, 99999999))
#     number = prefix + str(random.randint(100_000_000, 999_999_999))
#
#     return number
#
#
# phoneNumb = generate_phone_number()
#
# uid = random.randint(10_000_000_000, 20_000_000_000)
#
# regForm = {
#     "phoneNumb": str(phoneNumb),
#     "name": "This account",
#     "family": "uses for tests",
#     "ID": str(uid),
#     "storeName": "Shiva Store",
#     "address": "968 West Arcadia Drive New York, NY 10027",
#     "postalCode": "123456789",
#     "role_id": "103",
#     "storePhone": "02122306802"
# }
#
#
# def test_register(playwright: Playwright):
#     iphone_13 = playwright.devices['iPhone 13']
#     browser = playwright.webkit.launch(headless=False)
#     context = browser.new_context(
#         **iphone_13, record_video_dir="videos/")
#     context.tracing.start(screenshots=True, snapshots=True, sources=True)
#     page = context.new_page()
#     login_page = LoginPage(page)
#     login_page.navigate_to_login()
#     login_page.enter_phone(phone_number=regForm["phoneNumb"])
#     login_page.enter_password()
#     register_page = Registration(page)
#     register_page.should_see_form()
#     register_page.registering_form(name=regForm["name"], family=regForm["family"]
#                                    , uid=regForm["ID"], store_title=regForm["storeName"], address=regForm["address"],
#                                    postalcode=regForm["postalCode"], role_id=regForm["role_id"],
#                                    store_phone=regForm["storePhone"])
