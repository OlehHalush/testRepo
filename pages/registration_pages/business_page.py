import allure
from playwright.sync_api import Page

from pages.base_page import BasePage


class BusinessPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.__start_for_free_btn = "//button[text()='Start for free']"
        self.__login_btn = "//button[text()='Login']"

    @allure.step("open url to business site")
    def open_page(self):
        self.get_page().goto("/")
        return self

    @allure.step("click 'Start for free' button")
    def click_start_for_free(self):
        with self.get_context().expect_page() as new_page:
            self.locator(self.__start_for_free_btn).click()
            new_tab = new_page.value
            new_tab.set_default_timeout(60*1000)
            new_tab.set_default_navigation_timeout(60*1000)
        from pages.registration_pages.create_account_page import CreateAccountPage
        return CreateAccountPage(new_tab), new_tab

    @allure.step("click 'Login'' button")
    def click_login(self):
        self.locator(self.__login_btn).click()
        from pages.login_page import LoginPage
        return LoginPage(self.get_page())
