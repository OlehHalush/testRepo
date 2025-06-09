import re

import allure
from playwright.sync_api import Page, expect

from pages.base_page import BasePage


class CreateAccountPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.__header = "div.section-flex-left div.heading-medium"
        self.__name_input = "#FullName"
        self.__business_email_input = "#Email"
        self.__password_input = "#Password"
        self.__sign_up_btn = "button.button-login"

    @allure.step("enter name '{1}'")
    def enter_name(self, name):
        self.locator(self.__name_input).fill(name)
        return self

    @allure.step("enter business email '{1}'")
    def enter_business_email(self, email):
        self.locator(self.__business_email_input).fill(email)
        return self

    @allure.step("enter password '{1}'")
    def enter_password(self, password):
        self.locator(self.__password_input).click()
        self.get_page().keyboard.type(password)
        return self

    @allure.step("click 'Sign up' button")
    def click_sign_up(self):
        self.locator(self.__sign_up_btn).click()
        return self

    @allure.step("verify page header is '{1}'")
    def verify_page_header(self, header: str):
        expect(self.locator(self.__header)).to_contain_text(header)
        return self

    @allure.step("verify 'Sign up' button is enabled '{1}'")
    def verify_sign_up_button_is_enabled(self, is_enabled):
        btn_locator = self.locator(self.__sign_up_btn)
        btn_locator.wait_for(state="attached")
        if is_enabled:
            expect(btn_locator).to_have_class(re.compile(r".*\bbutton-enabled.*\b.*"))
        else:
            expect(btn_locator).to_have_class(re.compile(r".*\bbutton-disabled.*\b.*"))
        return self
