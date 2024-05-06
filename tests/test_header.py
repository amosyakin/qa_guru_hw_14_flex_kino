import allure
import pytest
from allure_commons.types import Severity

from gu_guru_hw_14_flex_kino.model.pages.general_page import GeneralPage
from gu_guru_hw_14_flex_kino.model.pages.header import Header
from gu_guru_hw_14_flex_kino.model.pages.page import Page


@allure.tag("WEB")
@allure.severity(Severity.NORMAL)
@allure.feature('Header')
@allure.issue('https://jira.autotests.cloud/browse/HOMEWORK-1212')
@pytest.mark.parametrize("menu", ['Сериалы', 'Фильмы', 'Подборки', 'Тарифы'])
class TestHeaderMenu:

    @allure.title('Переход в раздел {menu}')
    def test_open_serial_catalog_from_header(self, setup_browser, menu):
        with allure.step('Открытие главной страницы'):
            general_page = GeneralPage()
            general_page.open()

        with allure.step('В хэдэре перейти в раздел {menu}'):
            header = Header()
            header.click_menu(menu)
            page = Page()
            page.should_page_title(menu)
