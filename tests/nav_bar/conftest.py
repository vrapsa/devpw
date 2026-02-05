import pytest
from playwright.sync_api import Page

from pom.main.nav_bar import NavBar


@pytest.fixture
def nav_bar(page: Page) -> NavBar:
    return NavBar(page)