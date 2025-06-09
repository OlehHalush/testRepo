import allure
from playwright.sync_api import Page, expect

from pages.base_page import BasePage


class ThanksForConfirmingEmailPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.__title = "div.text-landing h1"
        self.__enter_dashboard_link = "//a[normalize-space()='Enter your dashboard']"

    @allure.step("click 'Enter dashboard' link")
    def click_enter_dashboard_link(self):
        self.locator(self.__enter_dashboard_link).click()
        from pages.registration_pages.welcome_page import WelcomePage
        return WelcomePage(self.get_page())

    @allure.step("verify 'Thanks for confirming email' page title is 'Thanks for confirming your email!'")
    def verify_title(self):
        expect(self.locator(self.__title)).to_have_text("Thanks for confirming your email!")
        return self
