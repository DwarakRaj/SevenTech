from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class WebDriverFactory:

    def open_browser(self):
        '''This method generate the driver'''
        '''ChromeDriverManager is used to automatically manage drivers for different browsers. No need for browser 
        executable file '''
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.implicitly_wait(10)
        driver.maximize_window()
        return driver
