from selene import browser, command, by


class Footer:

    def __init__(self):
        self.footer = browser.element('.footer')
        self.footer_menu = browser.element('.menu-button')
        self.app_icon = browser.element('.footer__applications')

    def scroll_to_footer(self):
        self.footer.perform(command.js.scroll_into_view)

    def click_button(self, button_name):
        self.footer_menu.element(by.text(button_name)).click()

    def click_app_icons(self, app_name):
        self.app_icon.element(f'img[alt="{app_name}"]').click()