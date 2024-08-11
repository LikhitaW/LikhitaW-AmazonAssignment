import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chrOptions
from utilities.readProperty import ReadConfigProperty



@pytest.fixture()
def setup():
    browser = ReadConfigProperty("common info","browser")
    global web_driver
    web_driver = None
    if browser.lower() == "chrome":
        chrome_options = chrOptions()
        chrome_options.add_argument("'--disable-blink-features=AutomationControlled'")
        web_driver = webdriver.Chrome(options=chrome_options)
    elif browser.lower() == "firefox":
        web_driver = webdriver.Firefox()
    elif browser.lower() == "edge":
        web_driver = webdriver.Edge()
    web_driver.implicitly_wait(5)
    web_driver.maximize_window()
    baseurl = ReadConfigProperty("common info","baseurl")
    web_driver.get(baseurl)
    return web_driver

@pytest.fixture()
def teardown():
    yield
    web_driver.quit()