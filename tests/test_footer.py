import allure
from allure_commons.types import Severity

from gu_guru_hw_14_flex_kino.model.pages.footer import footer
from gu_guru_hw_14_flex_kino.model.pages.general_page import general_page
from gu_guru_hw_14_flex_kino.model.pages.page import page


@allure.tag("WEB")
@allure.severity(Severity.NORMAL)
@allure.feature('Footer')
@allure.issue('https://jira.autotests.cloud/browse/HOMEWORK-1212')
class TestFooter:

    @allure.title('Открытие страницы Документы правообладателей')
    def test_open_copyright(self, setup_browser):
        general_page.open()
        footer.scroll_to_footer()
        footer.click_button('Документы правообладателей')
        page.should_page_title('Документы правообладателей')

    @allure.title('Переход на страницу Android RuStore')
    def test_rustore_link(self, setup_browser):
        general_page.open()
        footer.scroll_to_footer()
        footer.click_app_icons('rustore')
        page.should_url_redirect("https://www.rustore.ru/catalog/app/films.android")
