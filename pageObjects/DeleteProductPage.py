from selenium.webdriver.common.by import By
from utilities import seleniumFunctions


class DeleteProductPage:

    del_product = (By.XPATH,"//input[contains(@name,'submit.delete.')]")
    empty_cart_msg = (By.XPATH, "//h1[contains(text(),'Your Amazon Cart is empty.')]")

    def __init__(self, driver):
        self.driver = driver

    def delete_product(self):
        seleniumFunctions.click_on_element(self,self.del_product)

    def verify_product_deleted(self):
        assert seleniumFunctions.check_element_displayed(self,self.empty_cart_msg)
