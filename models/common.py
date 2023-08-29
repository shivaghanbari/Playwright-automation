from playwright.sync_api import expect


class CommonTools:
    def __init__(self, page):
        self.page = page

    def check_page_is_loaded(self, page_title):
        title = self.page.get_by_text(page_title)
        try:
            expect(title).to_be_visible()
        except:
            self.page.reload()
            expect(title).to_be_visible()
