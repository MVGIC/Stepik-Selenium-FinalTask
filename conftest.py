import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action="store", default="en", help="Language is not supported")


@pytest.fixture(scope="function")
def browser(request):
    browser_language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': browser_language})
    print("\nstart chrome browser for test..")
    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(10)  # явное ожидание
    yield browser
    print("\nquit browser..")
    browser.quit()
