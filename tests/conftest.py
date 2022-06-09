import pytest
from Generics.webdriver_factory import WebDriverFactory


@pytest.fixture()
def one_time_set_up():
    wdf_obj = WebDriverFactory()
    driver = wdf_obj.open_browser()
    yield driver
    driver.quit()
