import allure
from allure_commons.types import Severity

from gu_guru_hw_14_flex_kino.model.pages.general_page import GeneralPage
from gu_guru_hw_14_flex_kino.model.pages.header import Header


@allure.tag("WEB")
@allure.severity(Severity.NORMAL)
@allure.feature('Хэдэр')
@allure.suite('Поиск')
@allure.issue('https://jira.autotests.cloud/browse/HOMEWORK-1212')
@allure.title('Выполнить поиск по контенту')
def test_search_by_content(setup_browser):
    with allure.step('Открытие главной страницы'):
        general_page = GeneralPage()
        general_page.open()

    with allure.step('Нажать на иконку "Поиск"'):
        header = Header()
        header.click_search_button()

    with allure.step('Ввести название контента "Оппенгеймер"'):
        header.type_content_to_search('Оппенгеймер')
        header.should_search_content('Оппенгеймер')
