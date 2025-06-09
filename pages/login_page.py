import re

import allure
from playwright.sync_api import Page, expect

from pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.__header = "div.section-flex-left div.heading-medium"
        self.__email_input = "#Email"
        self.__password_input = "#Password"
        self.__login_btn = "button#login"

    @allure.step("verify 'Login' page header is 'Welcome back to Rebrandly'")
    def verify_header(self):
        expect(self.locator(self.__header)).to_contain_text("Welcome back to Rebrandly")
        return self

    @allure.step("enter email '{1}'")
    def enter_email(self, email):
        self.locator(self.__email_input).fill(email)
        return self

    @allure.step("enter password '{1}'")
    def enter_password(self, password):
        self.locator(self.__password_input).click()
        self.get_page().keyboard.type(password)
        return self

    @allure.step("click 'Login' button")
    def click_login(self):
        self.locator(self.__login_btn).click()
        from pages.links_page import LinksPage
        return LinksPage(self.get_page())

    @allure.step("verify 'Login' button is enabled '{1}'")
    def verify_login_button_is_enabled(self, is_enabled):
        btn_locator = self.locator(self.__login_btn)
        btn_locator.wait_for(state="attached")
        if is_enabled:
            expect(btn_locator).to_have_class(re.compile(r".*\bbutton-enabled.*\b.*"))
        else:
            expect(btn_locator).to_have_class(re.compile(r".*\bbutton-disabled.*\b.*"))
        return self
