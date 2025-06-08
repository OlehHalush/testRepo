import allure
from playwright.sync_api import Page, BrowserContext, expect

from pages.base_page import BasePage
from pages.create_account_page import CreateAccountPage


class BusinessPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.start_for_free_btn = "//button[text()='Start for free']"

    @allure.step("open url to business site")
    def open_page(self):
        self.get_page().goto("/")
        return self

    @allure.step("click 'Start for free' button")
    def click_start_for_free(self):
        with self.get_context().expect_page() as new_page:
            self.wait_for_page_loaded()
            self.locator(self.start_for_free_btn).click()
            new_tab = new_page.value
            new_tab.wait_for_load_state()
        return CreateAccountPage(new_tab), new_tab
