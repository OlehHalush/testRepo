import allure
from playwright.sync_api import Page, BrowserContext, expect

from pages.base_page import BasePage


class WelcomePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.title = ".OnBoardingWelcome__title"
        self.get_started_button = "button.Button--primary"

    @allure.step("verify Welcome page title is 'Welcome to Rebrandly!'")
    def verify_title(self):
        expect(self.locator(self.title)).to_have_text("Welcome to Rebrandly!", timeout=20000)
        return self

    @allure.step("verify  'Get Started' button is visible")
    def verify_get_started_btn_is_visible(self):
        expect(self.locator(self.get_started_button)).to_be_visible()
        return self

    @allure.step("click 'Get Started' button")
    def click_get_started(self):
        self.locator(self.get_started_button).click()
