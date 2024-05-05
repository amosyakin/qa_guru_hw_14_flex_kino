import allure
from allure_commons.types import Severity
from selene import browser, have


@allure.tag("WEB")
@allure.severity(Severity.NORMAL)
@allure.feature('Хэдэр')
@allure.suite('Поиск')
@allure.issue('https://jira.autotests.cloud/browse/HOMEWORK-1212')
@allure.title('Выполнить поиск по контенту')
def test_search_by_content(setup_browser):
    with allure.step('Открытие главной страницы'):
        browser.open("/")

    with allure.step('Нажать на иконку "Поиск"'):
        browser.element('.header .search').click()

    with allure.step('Ввести название контента "Оппенгеймер"'):
        browser.element('.search-input__control').type('Оппенгеймер')
        browser.element('.search__result').should(have.text('Оппенгеймер'))
