class Bookmark:
    def __init__(self, page):
        self.page = page

    # this function checks, if user has searched the target product in search-bar before.
    def check_search_history(self, target_product):

        product_in_history = self.page.get_by_text(target_product).first.is_visible()
        if product_in_history is True:
            print(target_product, " exists in your history")
            self.page.get_by_text(target_product).first.click()
        else:
            print("Can not find ", target_product, " fill it...")
            self.page.get_by_placeholder("جستجو در پین‌دیس").first.fill(target_product)

    # this function takes the target product from test file while running scenario and marks it.
    def set_bookmark(self, my_product):
        self.find_product_by_search_bar(product=my_product)
        # Auto-waiting.
        self.page.get_by_text("مبلغ قابل پرداخت").click()

        # bookmark icon include of two classes.one of them is empty state and the second one shows filled state.
        bookmark_locator = self.page.locator(".product-header-mobile_active-bookmark__2AoQc")
        if bookmark_locator.first.is_visible():
            bookmark_locator.first.click()
            print("bookmark is removed.")
        else:
            bookmark_locator = self.page.locator(".product-header-mobile_bookmark__3YT94")
            bookmark_locator.first.click()
            print(my_product, " added to bookmark list.")

        # user clicks on home page to run for second time.
        self.page.get_by_role("button", name="خانه").click()

    # user can find product in two ways,directly and un-directly.first method attempts to find product by searching
    # in search bar and in second one, user tries to reach it by scrolling and click on brands etc.
    def find_product_by_search_bar(self, product):
        self.page.get_by_placeholder("جستجو در پین‌دیس").first.click()
        self.check_search_history(target_product=product)
        self.page.get_by_role("img", name="category").first.click()
