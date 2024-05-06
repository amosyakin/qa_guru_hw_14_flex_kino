from selene import browser, by, have, command


class GeneralPage:
    def open(self):
        browser.open('/')
        return self
