import allure
from playwright.sync_api import Page, BrowserContext, expect

from pages.base_page import BasePage
from pages.welcome_page import WelcomePage


class ThanksForConfirmingEmailPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.title = "div.text-landing h1"
        self.enter_dashboard_link = "//a[normalize-space()='Enter your dashboard']"

    @allure.step("click 'Enter dashboard' link")
    def click_enter_dashboard_link(self):
        self.locator(self.enter_dashboard_link).click()
        return WelcomePage(self.get_page())

    @allure.step("verify 'Thanks for confirming email' page title is 'Thanks for confirming your email!'")
    def verify_title(self):
        expect(self.locator(self.title)).to_have_text("Thanks for confirming your email!")
        return self
