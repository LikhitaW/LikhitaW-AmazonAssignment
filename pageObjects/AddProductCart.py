from selenium.webdriver.common.by import By
from utilities import seleniumFunctions

class AddProductCartPage:
    view_cart = (By.XPATH, "//a[@href='/gp/cart/view.html?ref_=nav_cart']")
    view_quantity = (By.XPATH, "//span[@class='a-dropdown-prompt']")
    view_price = (By.XPATH, "//span[@id='sc-subtotal-amount-activecart']")
    add_quantity = (By.XPATH,"//span[@class='a-dropdown-container']//select")

    def __init__(self,driver):
        self.driver = driver

    def add_product(self,id):
        item_search = (By.XPATH, f"(//div[contains(@class,'sg-col-20-of-24 s-result-')])[{id}]")
        product_name = (By.XPATH, f"(//div[@class='puisg-col-inner']//h2)[{id}]")
        add_to_cart = (By.XPATH, f"(//button[text()='Add to cart'])[{id}]")
        seleniumFunctions.scroll_element(self,item_search)
        prod_name = seleniumFunctions.get_text_on_element(self,product_name)
        seleniumFunctions.scroll_element(self,add_to_cart)
        seleniumFunctions.click_on_element(self,add_to_cart)
        return prod_name

    def click_view_cart(self):
        seleniumFunctions.click_on_element(self,self.view_cart)

    def verify_product_added(self):
        assert seleniumFunctions.check_element_displayed(self,self.view_price)

    def view_product_details(self):
        price= seleniumFunctions.get_text_on_element(self,self.view_price)
        quant = seleniumFunctions.get_text_on_element(self,self.view_quantity)
        prod_details = [price,quant]
        return prod_details

    def update_quantity(self,quant):
        select_quant_dropdown = (By.XPATH, f"//div[@class='a-popover-wrapper']//ul/li/a[text()='{quant}']")
        seleniumFunctions.execute_click_element(self,self.add_quantity)
        seleniumFunctions.click_on_element(self,select_quant_dropdown)

