import allure
from allure_commons.types import Severity

from gu_guru_hw_14_flex_kino.model.pages.footer import Footer
from gu_guru_hw_14_flex_kino.model.pages.general_page import GeneralPage
from gu_guru_hw_14_flex_kino.model.pages.page import Page


@allure.tag("WEB")
@allure.severity(Severity.NORMAL)
@allure.feature('Footer')
@allure.issue('https://jira.autotests.cloud/browse/HOMEWORK-1212')
class TestFooter:

    @allure.title('Открытие страницы Документы правообладателей')
    def test_open_copyright(self, setup_browser):
        with allure.step('Открытие главной страницы'):
            general_page = GeneralPage()
            general_page.open()

        with allure.step('Пролистать до футера'):
            footer = Footer()
            footer.scroll_to_footer()

        with allure.step('Нажать на кнопку "Документы правообладателей"'):
            footer.click_button('Документы правообладателей')
            page = Page()
            page.should_page_title('Документы правообладателей')

    @allure.title('Переход на страницу Android RuStore')
    def test_rustore_link(self, setup_browser):
        with allure.step('Открытие главной страницы'):
            general_page = GeneralPage()
            general_page.open()

        with allure.step('Пролистать до футера'):
            footer = Footer()
            footer.scroll_to_footer()

        with allure.step('Нажать на кнопку "RuStore"'):
            footer.click_app_icons('rustore')
            page = Page()
            page.should_url_redirect("https://www.rustore.ru/catalog/app/films.android")
