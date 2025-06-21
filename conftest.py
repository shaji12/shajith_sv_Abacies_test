import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from  webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="class")
def setup(req):
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    req.cls.driver = driver
    yield
    driver.quit()