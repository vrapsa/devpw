import time
from typing import Literal

from loguru import logger
from playwright.sync_api import Page, Locator

from helpers.base_page import BasePage
from pom.main.search_modal import SearchModal


class NavBar(BasePage):

    LANGUAGES = ["Java", ".NET", "Python", "Node.js"]
    LANGUAGE_PARAM = Literal["Java", ".NET", "Python", "Node.js"]

    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self._root = self.page.get_by_role("navigation", name="main")

        # Общая навигация
        self._dynamic_link = self._root.get_by_role("link", name="Playwright")
        self.logo = self._dynamic_link.get_by_alt_text("Playwright logo")
        self.text = self._dynamic_link.locator("//b[contains(text(), 'Playwright')]")
        self.docs = self._root.get_by_role("link", name="Docs")
        self.api = self._root.get_by_role("link", name="API")
        self.community = self._root.get_by_role("link", name="Community")

        # Навигация языка
        self.language_dropdown = self._root.locator(".dropdown")

        # Ссылки
        self.github = self._root.get_by_role("link", name="GitHub repository")
        self.discord = self._root.get_by_role("link", name="Discord server")
        self.theme = self._root.get_by_role("button", name="Switch")
        self.search = self._root.get_by_role("button", name="Search")


    # Методы dropdown
    def available_languages(self, language: LANGUAGE_PARAM) -> Locator:
        self.language_dropdown.hover()
        return self.language_dropdown.get_by_role("link", name=language)

    def change_language(self, dropdown_language: LANGUAGE_PARAM) -> None:
        self.language_dropdown.hover()
        time.sleep(1)
        element = self.language_dropdown.get_by_role("link", name=dropdown_language)
        with self.page.expect_navigation(wait_until="domcontentloaded"):
            element.click()
        logger.debug(f"\nСмена языка программирования документации: {dropdown_language}")

    # Методы search
    def open_search(self) -> SearchModal:
        self.search.click()
        logger.debug(f"\nОткрыто модальное окно поиска")
        return SearchModal(self.page)
