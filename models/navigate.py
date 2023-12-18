# This function is used for intercepting network requests and making decisions based on the request URL.
# If the request URL contains the word "google," it will block the request and print a message indicating
# that it's being blocked. Otherwise, it allows the request to continue.
def rout_intercept(route):
    if "google" in route.request.url:
        print(f"blocking {route.request.url} as it contains Google")
        return route.abort()
    return route.continue_()


# Open website
class Navigate:
    def __init__(self, page):
        self.page = page

    def navigate(self):
        self.page.route("**/*", rout_intercept)
        self.page.goto("https://dribbble.com/")
