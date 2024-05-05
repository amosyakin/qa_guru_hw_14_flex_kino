import allure
from allure_commons.types import Severity
from selene import browser, by, have, command


@allure.tag("WEB")
@allure.severity(Severity.NORMAL)
@allure.feature('Футер')
@allure.issue('https://jira.autotests.cloud/browse/HOMEWORK-1212')
@allure.title('Открытие страницы Документы правообладателей')
def test_open_copyright(setup_browser):
    with allure.step('Открытие главной страницы'):
        browser.open("/")

    with allure.step('Пролистать до футера'):
        browser.element('.footer').perform(command.js.scroll_into_view)

    with allure.step('Нажать на кнопку "Документы правообладателей"'):
        browser.element('.menu-button').element(by.text('Документы правообладателей')).click()
        browser.element('.container__title').should(have.text('Документы правообладателей'))


@allure.tag("WEB")
@allure.severity(Severity.NORMAL)
@allure.feature('Футер')
@allure.issue('https://jira.autotests.cloud/browse/HOMEWORK-1212')
@allure.title('Переход на страницу Android RuStore')
def test_rustore_link(setup_browser):
    with allure.step('Открытие главной страницы'):
        browser.open("/")

    with allure.step('Пролистать до футера'):
        browser.element('.footer').perform(command.js.scroll_into_view)

    with allure.step('Нажать на кнопку "RuStore"'):
        browser.element('.footer__applications').element('img[alt="rustore"]').click()
        browser.should(have.url('https://apps.rustore.ru/app/films.android'))
