import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(params = ['chrome'],scope ='class')
def init_driver(request):
    if request.param == 'chrome':
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        request.cls.driver = driver
        yield
        driver.close()



def pytest_addoption(parser):
        parser.addoption('--browser')

@pytest.fixture()
def browser(request):
        return request.config.getoption('--browser')

#pytest Testcases/test_Login.py -s