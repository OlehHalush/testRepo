import allure
from playwright.sync_api import Page, BrowserContext, expect

from pages.base_page import BasePage


class CheckEmailPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.title = "div.text-landing h1"
        self.email = "div.text-landing h3 strong"

    @allure.step("verify 'Check email' page title is 'Please check your email!'")
    def verify_title(self):
        expect(self.locator(self.title)).to_have_text("Please check your email!")
        return self

    @allure.step("verify email is '{1}'")
    def verify_email(self, email):
        expect(self.locator(self.email)).to_have_text(email)
        return self
