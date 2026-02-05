import allure
import pytest
from playwright.sync_api import expect

from pom.main.nav_bar import NavBar

@allure.label("platform", "Автотесты")
@allure.label("module", "WEB")
@allure.label("feature", "Навигация")
@allure.label("part", "Шапка сайта")
class TestNavBar:

    @allure.id(1)
    @allure.title("Проверить видимость всех элементов навигации")
    @pytest.mark.smoke
    def test_nav_bar(self, nav_bar: NavBar):
        with allure.step("Проверить видимость логотипа"):
            expect(nav_bar.logo).to_be_visible()
        with allure.step("Проверить видимость общей навигации"):
            expect(nav_bar.logo).to_be_visible()
            expect(nav_bar.text).to_be_visible()
            expect(nav_bar.text).to_have_text("Playwright")
            expect(nav_bar.docs).to_be_visible()
            expect(nav_bar.api).to_be_visible()
            expect(nav_bar.community).to_be_visible()
        with allure.step("Проверить наличие вложенной навигации по языкам программирования"):
            for language in nav_bar.LANGUAGES:
                expect(nav_bar.available_languages(language)).to_be_visible()
        with allure.step("Проверить наличие кнопок-ссылок"):
            expect(nav_bar.discord).to_be_visible()
            expect(nav_bar.github).to_be_visible()
            expect(nav_bar.theme).to_be_visible()
        with allure.step("Проверить наличие поисковой строки"):
            expect(nav_bar.search).to_be_visible()
            expect(nav_bar.search).to_contain_text("Search")

    @allure.id(2)
    @allure.title("Проверить возможность смены языка программирования документации")
    @pytest.mark.smoke
    def test_change_site_language(self, nav_bar: NavBar):
        for language in nav_bar.LANGUAGES:
            nav_bar.change_language(language)
            if language == "Node.js":
                expect(nav_bar.text).to_have_text(f"Playwright")
            else:
                expect(nav_bar.text).to_have_text(f"Playwright for {language}")
