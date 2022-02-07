from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver_service = Service(executable_path="C:\\Users\\Anastasy MTT\\PycharmProjects\\chromedriver.exe")

def pytest_addoption(parser):
    parser.addoption("--language", action='store', default='en',
                     help="Choose language:")

@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption('language')
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})

    browser = webdriver.Chrome(
        service=driver_service, options=options)

    browser.implicitly_wait(15)
    yield browser
    browser.quit()
