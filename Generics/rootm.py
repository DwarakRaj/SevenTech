from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementNotVisibleException
from utilities.util import read_data_from_excel

path_to_locators = "D:\\MYPROJECTS\\SevenTechAssignments\\Pages\\testdata\\locators.xlsx"


def enter_url(driver, base_url):
    '''This method will enter given url in the search bar'''
    driver.get(base_url)


def get_element(driver, element_name):
    ''' This method find a single element on the current web page by retrieving locators details from excel sheet '''

    locator_type = read_data_from_excel(path_to_locators, "login_page", element_name=element_name,
                                        locator_type=True)
    locator_value = read_data_from_excel(path_to_locators, "login_page", element_name=element_name,
                                         locator_value=True)

    locator_type = locator_type.lower()

    if locator_type == "tagname":
        by_locator_obj = By.TAG_NAME
    elif locator_type == "id":
        by_locator_obj = By.ID
    elif locator_type == "name":
        by_locator_obj = By.NAME
    elif locator_type == "classname":
        by_locator_obj = By.CLASS_NAME
    elif locator_type == "linktext":
        by_locator_obj = By.LINK_TEXT
    elif locator_type == "partiallinktext":
        by_locator_obj = By.PARTIAL_LINK_TEXT
    elif locator_type == "cssselector":
        by_locator_obj = By.CSS_SELECTOR
    elif locator_type == "xpath":
        by_locator_obj = By.XPATH
    else:
        raise ValueError("locator type is invalid")

    try:
        element = driver.find_element(by_locator_obj, locator_value)
        return element
    except ElementNotVisibleException:
        print("Element Not Found")
        return None


def get_elements(driver, element_name):
    ''' This method find a multiple elements on the current web page by retrieving locators details from excel sheet '''

    locator_type = read_data_from_excel(path_to_locators, "login_page", element_name=element_name,
                                        locator_type=True)
    locator_value = read_data_from_excel(path_to_locators, "login_page", element_name=element_name,
                                         locator_value=True)

    locator_type = locator_type.lower()

    if locator_type == "tagname":
        by_locator_obj = By.TAG_NAME
    elif locator_type == "id":
        by_locator_obj = By.ID
    elif locator_type == "name":
        by_locator_obj = By.NAME
    elif locator_type == "classname":
        by_locator_obj = By.CLASS_NAME
    elif locator_type == "linktext":
        by_locator_obj = By.LINK_TEXT
    elif locator_type == "partiallinktext":
        by_locator_obj = By.PARTIAL_LINK_TEXT
    elif locator_type == "cssselector":
        by_locator_obj = By.CSS_SELECTOR
    elif locator_type == "xpath":
        by_locator_obj = By.XPATH
    else:
        raise ValueError("locator type is invalid")

    try:
        elements = driver.find_elements(by_locator_obj, locator_value)
        return elements
    except ElementNotVisibleException:
        print("Element Not Found")
        return None


def send_values(driver, element_name, value):
    ''' This method enter any value in a text box'''
    try:
        get_element(driver, element_name).send_keys(value)
    except Exception:
        print("not valid element")


def click_on_element(driver, element_name):
    '''Ths method clicks on given element'''
    try:
        get_element(driver, element_name).click()
    except Exception:
        print("not valid element")


def get_element_text(driver, element_name):
    '''This method used to find given element's text'''
    try:
        text = get_element(driver, element_name).text
        return text
    except Exception:
        print("not valid element")
