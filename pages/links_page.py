from playwright.sync_api import Page

from pages.top_menu_bar import TopMenuBar


class LinksPage(TopMenuBar):
    def __init__(self, page: Page):
        super().__init__(page)
