from selenium.webdriver.common.by import By
from utilities import seleniumFunctions
from utilities.readProperty import ReadConfigProperty

class SearchProductPage:
    invalid_item = ReadConfigProperty("common info", "invalid_item")
    valid_item = ReadConfigProperty("common info", "valid_item")

    search_box = (By.ID,"twotabsearchtextbox")
    search_icon = (By.XPATH,"//input[@id='nav-search-submit-button']")
    no_result_msg = (By.XPATH,"//div[@class='a-section a-spacing-none']//following::span[text()='No results for ']")
    valid_msg=(By.XPATH,"//div[@class='s-no-outline']/h2[text()='Results']")

    def __init__(self,driver):
        self.driver = driver

    def search_product(self,item):
        seleniumFunctions.enter_text_on_element(self,self.search_box,item)
        seleniumFunctions.click_on_element(self,self.search_icon)

    def verify_msg_search_item(self,item):
       if item== self.valid_item:
           bln_flg = seleniumFunctions.check_element_displayed(self,self.valid_msg)
           return bln_flg
       elif item==self.invalid_item:
            bln_flg = seleniumFunctions.check_element_displayed(self,self.no_result_msg)
            return bln_flg