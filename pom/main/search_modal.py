import re

from loguru import logger
from playwright.sync_api import Page, Locator

from helpers.base_page import BasePage


class SearchModal(BasePage):
    """ Модальное окно поиска"""

    def __init__(self, page: Page):
        super().__init__(page)
        self._root = self.page.locator("div.DocSearch-Modal")

        # Модальное окно поиска
        self.header = self._root.locator("header")
        self.dropdown = self._root.locator("div.DocSearch-Dropdown")
        self.footer = self._root.locator("footer")

    # Методы, возвращающие локаторы
    @property
    def see_no_results(self) -> Locator:
        return self.dropdown.get_by_text("No recent searches", exact=True)

    @property
    def see_all_results(self) -> Locator:
        return self.dropdown.get_by_role("link", name=re.compile("See all"))

    @property
    def section_results(self) -> Locator:
        """ Если к методу необходимо применить all(), то для корректной работы в тесте
        необходимо ждать видимость первого элемента """
        return self.dropdown.locator("section")

    @property
    def clear_query(self):
        return self.header.get_by_role("button", name="Clear the query")

    # Методы действий
    def fill_search(self, text: str) -> None:
        self.header.locator("input").fill(text)
        logger.debug(f"\nПоисковый запрос: {text}")