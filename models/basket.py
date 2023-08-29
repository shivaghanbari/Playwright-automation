from playwright.sync_api import expect


class BasketPage:
    def __init__(self, page):
        self.page = page 

    def click_basket(self):
        self.page.get_by_role("button", name="سبد").click()

    def basket_has_items(self):
        submit_button = self.page.get_by_role("button", name="ادامه خرید")
        try:
            expect(submit_button).to_be_visible()
            return True
        except:
            return False
        
    def empty_basket(self):
        self.page.locator(".general-header-mobile_search-icon__qdG6u > .MuiSvgIcon-root").first.click()
        self.page.get_by_role("button", name="بله، حذف شود.").click()

    def add_to_basket(self):
        self.page.get_by_role("button", name="خانه").click()
        self.page.locator(".home_collections-container-mobile__2SNQF > div:nth-child(5) > .product-collection_scrolling-wrapper__1LBM7 > div > .vertical-product-card_footer__2E9t3 > .false").first.click()

    def submit_basket(self):
        self.page.get_by_role("button", name="ادامه خرید").click()