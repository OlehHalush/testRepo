import re
from typing import Literal

import allure
from playwright.sync_api import Page, expect

from pages.base_page import BasePage


class TopMenuBar(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.__menu_btn_by_name = "//li[.//*[text()='{}']]"
        self.__account_btn = "div.MainHeaderAccount__dropdown"
        self.__acc_name_from_acc_panel = "div.AccountPanel p.Text--Detail"
        self.__acc_email_from_acc_panel = "div.AccountPanel p.Text--x-small"
        self.__account_settings_link_from_acc_panel = "a[rb-test-id='account-settings-item']"
        self.__subscription_link_from_acc_panel = "a[rb-test-id='account-subscription-item']"
        self.__payment_method_link_from_acc_panel = "a[rb-test-id='account-payment-method-item']"
        self.__billing_and_contact_data_link_from_acc_panel = "a[rb-test-id='account-billing-data-item']"
        self.__billing_history_link_from_acc_panel = "a[rb-test-id='account-billing-history-item']"
        self.__api_link_from_acc_panel = "a[rb-test-id='account-api-keys-item']"
        self.__top_features_link_from_acc_panel = "a[rb-test-id='navigate-to-integrations']"
        self.__request_support_link_from_acc_panel = "//a[text()='Request support']"
        self.__talk_to_sales_link_from_acc_panel = "a[rb-test-id='talk-to-sales-item']"
        self.__sign_out_link_from_acc_panel = "a[rb-test-id='account-sign-out-item']"

    @allure.step("select '{1}}' menu")
    def select_links_menu(
            self,
            menu_name: Literal[
                "Links", "Reports", "Workspaces", "Teammates", "Domains",
                "Integrations", "Pricing", "Link Gallery"]):
        self.locator(self.__menu_btn_by_name.format(menu_name)).click()
        if menu_name == "Links":
            from pages.links_page import LinksPage
            return LinksPage(self.get_page())

    @allure.step("verify '{1}' menu is selected")
    def verify_menu_is_selected(
            self,
            menu_name: Literal[
                "Links", "Reports", "Workspaces", "Teammates", "Domains",
                "Integrations", "Pricing", "Link Gallery"],
            is_selected):
        menu_locator = self.locator(self.__menu_btn_by_name.format(menu_name))
        menu_locator.wait_for(state="attached")
        if is_selected:
            expect(menu_locator).to_have_class(re.compile(r".*\bactive.*\b.*"))
        else:
            expect(menu_locator).not_to_have_class(re.compile(r".*\bactive.*\b.*"))
        return self

    @allure.step("click Account button")
    def click_account_button(self):
        self.locator(self.__account_btn).click()
        return self

    @allure.step("select '{1}' option from account panel")
    def select_option_from_account_panel(
            self,
            option: Literal[
                "Account settings", "Subscription", "Payment method", "Billing and contact data", "Billing history",
                "API", "Top features", "Request support", "Talk to sales", "Sign out"]):
        if option == "Account settings":
            self.locator(self.__account_settings_link_from_acc_panel).click()
        if option == "Subscription":
            self.locator(self.__subscription_link_from_acc_panel).click()
        if option == "Payment method":
            self.locator(self.__payment_method_link_from_acc_panel).click()
        if option == "Billing and contact data":
            self.locator(self.__billing_and_contact_data_link_from_acc_panel).click()
        if option == "Billing history":
            self.locator(self.__billing_history_link_from_acc_panel).click()
        if option == "API":
            self.locator(self.__api_link_from_acc_panel).click()
        if option == "Top features":
            self.locator(self.__top_features_link_from_acc_panel).click()
        if option == "Request support":
            self.locator(self.__request_support_link_from_acc_panel).click()
        if option == "Talk to sales":
            self.locator(self.__talk_to_sales_link_from_acc_panel).click()
        if option == "Sign out":
            self.locator(self.__sign_out_link_from_acc_panel).click()
            from pages.logout_page import LogoutPage
            return LogoutPage(self.get_page())

    @allure.step("verify account name in account panel is '{1}'")
    def verify_acc_name_from_acc_panel(self, acc_name):
        expect(self.locator(self.__acc_name_from_acc_panel)).to_have_text(acc_name)
        return self

    @allure.step("verify account email in account panel is '{1}'")
    def verify_acc_email_from_acc_panel(self, acc_email):
        expect(self.locator(self.__acc_email_from_acc_panel)).to_have_text(acc_email)
        return self
