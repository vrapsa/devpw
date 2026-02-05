import allure
import pytest
from playwright.sync_api import expect

from pom.main.nav_bar import NavBar
from pom.main.search_modal import SearchModal
from utils.allure.CommonSteps import CommonSteps


@allure.label("platform", "Автотесты")
@allure.label("module", "WEB")
@allure.label("feature", "Поиск")
@allure.label("part", "Блок поиска")
class TestSearch:

    @pytest.fixture
    def search_keyword(self, nav_bar: NavBar) -> SearchModal:
        with allure.step(CommonSteps.PREPARE_TEST_DATA):
            search_keyword = "locators"
        with allure.step("Нажать на строку поиска"):
            search = nav_bar.open_search()
        with allure.step("Ввести искомое слово"):
            search.fill_search(search_keyword)
            return search

    @allure.id(3)
    @allure.title("Проверить видимость всех блоков модального окна поиска")
    @pytest.mark.smoke
    def test_search_modal(self, nav_bar: NavBar):
        with allure.step("Открыть модальное окно поиска"):
            search = nav_bar.open_search()
        with allure.step("Проверить, что нет никаких результатов"):
            expect(search.see_no_results).to_be_visible()
        with allure.step("Проверить видимость блоков модального окна поиска"):
            for locator in [search.header, search.dropdown, search.footer]:
                expect(locator).to_be_visible()

    @allure.id(4)
    @allure.title("Проверить видимость найденных пресетов после ввода поискового запроса")
    @pytest.mark.smoke
    def test_search_presets(self, nav_bar: NavBar, search_keyword: SearchModal):
        search = search_keyword
        with allure.step("Проверить отображение блоков с пресетами"):
            expect(search.section_results.first).to_be_visible()
            for loc in search.section_results.all():
                expect(loc).to_be_visible()
        with allure.step("Проверить отображение 'Посмотреть еще'"):
            expect(search.see_all_results).to_be_visible()

    @allure.id(5)
    @allure.title("Проверить возможность очистки поискового запроса")
    @pytest.mark.smoke
    def test_search_clear(self, search_keyword):
        search = search_keyword
        with allure.step("Проверить, что хотя бы самый первый блок пресетов отображается в модальном окне поиска"):
            expect(search.section_results.first).to_be_visible()
        with allure.step("Очистить поисковый запрос, нажав на крестик в поле поиска"):
            search.clear_query.click()
        with allure.step("Проверить отсутствующие блоки пресетов"):
            expect(search.section_results).to_have_count(0)
        with allure.step("Проверить текст отсутствующего результата"):
            expect(search.see_no_results).to_be_visible()
