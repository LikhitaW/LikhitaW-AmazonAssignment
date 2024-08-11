import time
import pytest
from pageObjects.SearchProductPage import SearchProductPage
from pageObjects.AddProductCart import AddProductCartPage
from pageObjects.DeleteProductPage import DeleteProductPage
from utilities.readProperty import ReadConfigProperty
from utilities.customLogger import LogGen
from utilities import seleniumFunctions


class Test_001_ProductE2EFlow:
    driver = None
    invalid_item = ReadConfigProperty("common info","invalid_item")
    valid_item = ReadConfigProperty("common info","valid_item")
    prod_num = ReadConfigProperty("common info","prod_from_list")
    prod_name = None
    prod_details = None
    logger = LogGen.loggen()

    @pytest.mark.usefixtures("setup")
    def test_001_search_non_exist_product(self,setup):
        self.__class__.driver = setup
        self.searchProd = SearchProductPage(self.driver)
        self.searchProd.search_product(self.__class__.invalid_item)
        seleniumFunctions.capture_screenshot(self.searchProd,"Invalid Product search")
        bln_val = self.searchProd.verify_msg_search_item(self.__class__.invalid_item)
        if bln_val:
            self.logger.info("User is able to get message for non exist product")
            seleniumFunctions.capture_screenshot(self.searchProd,"User gets message for non exist product")
            assert True
        else:
            self.logger.info("User is unable to get message for non exist customer")
            assert False


    def test_002_search_exist_product(self):
        self.searchProd = SearchProductPage(self.driver)
        self.searchProd.search_product(self.__class__.valid_item)
        seleniumFunctions.capture_screenshot(self.searchProd,"User is able to search valid product")
        bln_val = self.searchProd.verify_msg_search_item(self.__class__.valid_item)
        if bln_val:
            self.logger.info("User is able to get message for existing product")
            seleniumFunctions.capture_screenshot(self.searchProd,"User is able to get results for products")
            assert True
        else:
            self.logger.info("User is unable to get message for existing customer")
            assert False

    def test_003_add_product_cart(self):
        self.addProd = AddProductCartPage(self.driver)
        self.__class__.prod_name = self.addProd.add_product(self.__class__.prod_num)
        seleniumFunctions.capture_screenshot(self.addProd,"User is able to add product")
        print("Prod name: ",self.__class__.prod_name)
        self.logger.info("Product gets selected to add")
        self.addProd.click_view_cart()
        seleniumFunctions.capture_screenshot(self.addProd,"Product gets viewed in cart")
        self.logger.info("Cart is viewed")
        self.addProd.verify_product_added()
        seleniumFunctions.capture_screenshot(self.addProd, "Product gets added successfully")
        self.logger.info("Product gets added to cart successfully")
        self.__class__.prod_details = self.addProd.view_product_details()
        print("Product Details: ",self.__class__.prod_details)

    def test_004_update_quantity(self):
        self.quantity=2
        self.addProd = AddProductCartPage(self.driver)
        self.addProd.click_view_cart()
        self.addProd.update_quantity(self.quantity)
        seleniumFunctions.capture_screenshot(self.addProd,"User is able to update the quantity")
        self.logger.info("Product quantity gets updated")
        self.__class__.update_prod_details = self.addProd.view_product_details()
        seleniumFunctions.capture_screenshot(self.addProd,"Product quantity gets updated")
        print("Product Details: ", self.__class__.update_prod_details)
        for i in range(2):
            if (self.__class__.prod_details[i]*2) == self.__class__.update_prod_details[i]:
                self.logger.info("Product gets incremented by 2")
                assert True

    def test_005_delete_product(self):
        self.addProd = AddProductCartPage(self.driver)
        self.addProd.click_view_cart()
        self.delProd = DeleteProductPage(self.driver)
        self.delProd.delete_product()
        seleniumFunctions.capture_screenshot(self.delProd,"User is able to delete product")
        self.logger.info("User is able to delete product")
        self.delProd.verify_product_deleted()
        seleniumFunctions.capture_screenshot(self.delProd,"Product gets removed from cart successfully")
        self.logger.info("Product gets deleted from cart")