import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


def pytest_addoption(parser):
    parser.addoption(
        '--browser_name',
        action='store',
        default='Chrome',
        help='Choose browser: Chrome or Firefox',
    )
    parser.addoption(
        '--language',
        action='store',
        default=None,
        help="Choose language: ",
        choices=(
            'ar',
            'ca',
            'cs',
            'da',
            'de',
            'en-gb',
            'el',
            'es',
            'fi',
            'fr',
            'it',
            'ko',
            'nl',
            'pl',
            'pt',
            'pt-br',
            'ro',
            'ru',
            'sk',
            'uk',
            'zh-hans',
        ),
    )


@pytest.fixture(scope='function')
def browser(request):
    browser_name = request.config.getoption('browser_name')
    language = request.config.getoption('language')

    print('\nStart browser for test')

    if browser_name == 'Chrome':
        service = Service(executable_path=ChromeDriverManager().install())
        browser_options = webdriver.ChromeOptions()
        browser_options.page_load_strategy = 'eager'
        # browser_options.add_argument('--headless')
        browser_options.add_experimental_option(
            'prefs', {'intl.accept_languages': language}
        )
        browser = webdriver.Chrome(service=service, options=browser_options)

    elif browser_name == 'Firefox':
        service = FirefoxService(executable_path=GeckoDriverManager().install())
        browser_options = webdriver.FirefoxOptions()
        browser_options.page_load_strategy = 'eager'
        browser_options.add_argument('--headless')
        browser_options.set_preference('intl.accept_languages', str(language))
        browser = webdriver.Firefox(service=service, options=browser_options)

    else:
        raise pytest.UsageError('--browser_name should be Chrome or Firefox')

    browser.maximize_window()
    browser.implicitly_wait(10)

    yield browser
    print('\nQuit browser after test')
    browser.quit()
