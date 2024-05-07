import allure
from allure_commons.types import Severity

from gu_guru_hw_14_flex_kino.model.pages.general_page import general_page
from gu_guru_hw_14_flex_kino.model.pages.header import header


@allure.tag("WEB")
@allure.severity(Severity.NORMAL)
@allure.feature('Хэдэр')
@allure.suite('Поиск')
@allure.issue('https://jira.autotests.cloud/browse/HOMEWORK-1212')
@allure.title('Выполнить поиск по контенту')
def test_search_by_content(setup_browser):
    general_page.open()
    header.click_search_button()
    header.type_content_to_search('Оппенгеймер')
    header.should_search_content('Оппенгеймер')
