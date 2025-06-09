import re

import allure
from playwright.sync_api import Page, expect

from pages.base_page import BasePage


class LogoutPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.__header = "div.section-flex-left div.heading-medium"
        self.__login_to_your_acc_link = "//a[text()='Log in to your account']"

    @allure.step("verify 'Logout' page header is 'You are logged out.'")
    def verify_title(self):
        expect(self.locator(self.__header)).to_contain_text("You are logged out.")
        return self

    @allure.step("verify 'Login to your account' button is enabled '{1}'")
    def verify_login_to_your_account_button_is_enabled(self, is_enabled):
        link_locator = self.locator(self.__login_to_your_acc_link)
        link_locator.wait_for(state="attached")
        if is_enabled:
            expect(link_locator).to_have_class(re.compile(r".*\bbutton-enabled.*\b.*"))
        else:
            expect(link_locator).to_have_class(re.compile(r".*\bbutton-disabled.*\b.*"))
        return self
