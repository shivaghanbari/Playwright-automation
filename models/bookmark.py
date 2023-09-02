
class Bookmark:
    def __init__(self, page):
        self.page = page

    def check_search_history(self):

        target_product = "پوشینه شورتی بزرگسال ایزی لایف متوسط 12 عددی"
        product_in_history = self.page.get_by_text(target_product).first.is_visible()
        if product_in_history is True:
            print(target_product, " exists in your history")
            self.page.get_by_text(target_product).first.click()
        else:
            print("Can not find ", target_product, " fill it")
            self.page.get_by_placeholder("جستجو در پین‌دیس").first.fill("پوشینه شورتی بزرگسال ایزی لایف متوسط 12 عددی")

    # user can find product in two ways,directly and un-directly.first method attempts to find product by searching
    # in search bar and in second one, user tries to reach it by scrolling and click on brands etc.
    def find_product_by_search_bar(self):
        self.page.get_by_placeholder("جستجو در پین‌دیس").first.click()
        self.check_search_history()
        self.page.get_by_text("پوشینه شورتی بزرگسال ایزی لایف متوسط 12 عددی").first.click()

    # def find_product_in_brand_list(self):
