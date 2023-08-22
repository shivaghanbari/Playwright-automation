from playwright.sync_api import expect


class HomePage:
    def __init__(self, page):
        self.page = page 

    def click_home(self):
        self.page.get_by_role("button", name="خانه").click()

    
