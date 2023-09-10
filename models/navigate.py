def rout_intercept(route):
    if "google" in route.request.url:
        print(f"blocking {route.request.url} as it contains Google")
        return route.abort()
    return route.continue_()


class Navigate:
    def __init__(self, page):
        self.page = page

    def navigate(self):
        self.page.route("**/*", rout_intercept)
        self.page.goto("https://dribbble.com/")
