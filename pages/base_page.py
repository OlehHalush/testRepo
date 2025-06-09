from abc import ABC

import allure
from playwright.sync_api import Page


class BasePage(ABC):
    def __init__(self, page: Page):
        self.__page = page
        self.__page.set_default_timeout(60*1000)
        self.__page.set_default_navigation_timeout(60*1000)

    def get_page(self):
        return self.__page

    def get_context(self):
        return self.__page.context

    @allure.step("open url '{1}'")
    def open_url(self, url):
        self.__page.goto(url)

    def locator(self, selector):
        return self.__page.locator(selector)

    def wait_for_page_loaded(self):
        self.__page.wait_for_load_state()
