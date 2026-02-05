import allure
import pytest
from playwright.sync_api import Page

import cfg


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    w, h = 1920, 1080
    return {
        **browser_context_args,
        "viewport": {"width": w, "height": h},
    }


@pytest.fixture(scope="function", autouse=True)
def before_each_after_each(page: Page):
    with allure.step("Зайти на главную страницу Playwright"):
        page.goto(cfg.URL)
    yield
