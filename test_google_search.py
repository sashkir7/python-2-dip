from selene import be, have
from selene.support.shared import browser

expected_selene_search_result = 'Selene - User-oriented Web UI browser tests in Python'


def test_search_selene_in_google(open_google):
    search_in_google('selene')
    browser.element('#search').should(have.text(expected_selene_search_result))


def test_do_not_search_selene_in_google(open_google):
    search_in_google('hello world!!!')
    browser.element('#search').should(have.no.text(expected_selene_search_result))


def search_in_google(value: str):
    browser.element('[name="q"]').should(be.blank).type(value).press_enter()
