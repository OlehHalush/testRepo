import allure
from playwright.sync_api import Page, expect

from pages.base_page import BasePage


class CheckEmailPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.__header = "div.text-landing h1"
        self.__email = "div.text-landing h3 strong"

    @allure.step("verify 'Check email' page title is 'Please check your email!'")
    def verify_title(self):
        expect(self.locator(self.__header)).to_have_text("Please check your email!")
        return self

    @allure.step("verify email is '{1}'")
    def verify_email(self, email):
        expect(self.locator(self.__email)).to_have_text(email)
        return self
