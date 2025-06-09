import allure
from playwright.sync_api import Page, expect

from pages.base_page import BasePage


class RegisterOrConnectDomainPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.__title = "div.SearchDomainsBox__title-wrapper p.Text--x-large"
        self.__skip_for_now_btn = "button[pendo-feature='domains-skip-at-signup']"

    @allure.step("verify 'Register or connect domain' page header is 'Register or connect a custom domain'")
    def verify_title(self):
        expect(self.locator(self.__title)).to_have_text("Register or connect a custom domain")
        return self

    @allure.step("click 'Skip for now' button")
    def click_skip_fow_now(self):
        self.locator(self.__skip_for_now_btn).click()
        from pages.links_page import LinksPage
        return LinksPage(self.get_page())
