from Generics.rootm import *
import requests
from time import sleep
import pytest
from selenium.webdriver.common.by import By

class Page:

    def __init__(self, driver):
        self.driver = driver

    def assert_broken_images(self, base_url):
        enter_url(self.driver, base_url)
        li = get_elements(self.driver, "image")
        print(len(li))
        broken_image_count = 0
        for i in range(0, len(li)):
            source = li[i].get_attribute('src')
            res = requests.get(source, stream=True)
            if res.status_code != 200:
                broken_image_count += 1
                print(li[i].get_attribute('outerHTML'))
        print('broken image count -  ', broken_image_count)

    def validate_invalid_login(self, base_url, un, pswd, error_msg):
        enter_url(self.driver, base_url)
        send_values(self.driver, "username_field", un)
        sleep(1)
        send_values(self.driver, "password_field", pswd)
        click_on_element(self.driver, "login_button")
        sleep(1)
        error_text = get_element_text(self.driver, "error_message")
        print(error_msg)
        print(error_text)
        assert str(error_msg) in str(error_text), 'error message not matching'

    def enter_random_alphabet(self, base_url, alphabet):
        enter_url(self.driver, base_url)
        send_values(self.driver, "number_field", alphabet)
        entered_text = get_element_text(self.driver, "number_field")
        assert str(alphabet) not in str(entered_text)," Field allowed alphabet"
        self.driver.save_screenshot("D:\\MYPROJECTS\\SevenTechAssignments\\screenshots\\image.png")
        pytest.fail('making the test case fail manually')

    def sort_table_data(self,base_url):
        enter_url(self.driver, base_url)
        dues = []
        for i in range(1,5):
            element = self.driver.find_element(By.XPATH, "((//table[@id='table1']/tbody/tr)["+str(i)+"]/td)[4]")
            dollar_value = element.text
            li = str(dollar_value).split('.')
            value = str(li[0]).split('$')
            dues.append(int(value[1]))
        print(dues)
        dues.sort()
        print("sorted dues----", dues)

    def render_success_message(self, base_url, success_msg):
        enter_url(self.driver, base_url)
        count = 1
        flag = True
        while count > 0 and flag == True:
            click_on_element(self.driver, "click_here_element")
            get_element(self.driver, "message_element")
            flash_text = get_element_text(self.driver, "message_element")
            if str(success_msg) in str(flash_text):
                flag = False
            else:
                count += 1
                flag = True
        print('number of clicks for work out- ', count)
