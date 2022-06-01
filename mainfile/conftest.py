from selenium import webdriver
import pytest
import allure

from Testdata.datareadwritefile import Datareadfile

driver = None

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    Url = Datareadfile.url
    global driver
    browser_name = request.config.getoption("--browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome(executable_path="G:\\chromedrivers\\chromedriver.exe")
    elif browser_name == "firefox":
        driver = webdriver.Firefox(executable_path='G:\\chromedrivers\\geckodriver.exe')
    elif browser_name == "edge":
        driver = webdriver.Firefox(executable_path='G:\\chromedrivers\\msedgedriver.exe')
    else:
        print("invalid browser text")
    driver.get(Url)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()