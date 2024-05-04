import allure
from allure_commons.types import Severity
from selene import browser, have, by


@allure.tag("WEB")
@allure.severity(Severity.NORMAL)
@allure.feature('Хэдэр')
@allure.link('https://jira.autotests.cloud/browse/HOMEWORK-1212')
@allure.title('Переход в раздел Сериалы')
def test_open_serial_catalog_from_header(setup_browser):
    with allure.step('Открытие главной страницы'):
        browser.open("/")

    with allure.step('В хэдэре перейти в раздел "Сериалы"'):
        browser.element('.header .menu').element(by.text('Сериалы')).click()
        browser.element('.container__title').should(have.text('Сериалы'))


@allure.tag("WEB")
@allure.severity(Severity.NORMAL)
@allure.feature('Хэдэр')
@allure.link('https://jira.autotests.cloud/browse/HOMEWORK-1212')
@allure.title('Переход в раздел Фильмы')
def test_open_film_catalog_from_header(setup_browser):
    with allure.step('Открытие главной страницы'):
        browser.open("/")

    with allure.step('В хэдэре перейти в раздел "Фильмы"'):
        browser.element('.header .menu').element(by.text('Фильмы')).click()
        browser.element('.container__title').should(have.text('Фильмы'))


@allure.tag("WEB")
@allure.severity(Severity.NORMAL)
@allure.feature('Хэдэр')
@allure.link('https://jira.autotests.cloud/browse/HOMEWORK-1212')
@allure.title('Переход в раздел Подборки')
def test_open_collection_from_header(setup_browser):
    with allure.step('Открытие главной страницы'):
        browser.open("/")

    with allure.step('В хэдэре перейти в раздел "Подборки"'):
        browser.element('.header .menu').element(by.text('Подборки')).click()
        browser.element('.container__title').should(have.text('Подборки'))


@allure.tag("WEB")
@allure.severity(Severity.NORMAL)
@allure.feature('Хэдэр')
@allure.link('https://jira.autotests.cloud/browse/HOMEWORK-1212')
@allure.title('Переход в раздел Тарифы')
def test_open_tariff_from_header(setup_browser):
    with allure.step('Открытие главной страницы'):
        browser.open("/")

    with allure.step('В хэдэре перейти в раздел "Тарифы"'):
        browser.element('.header .menu').element(by.text('Тарифы')).click()
        browser.element('.container__title').should(have.text('Тарифы'))
