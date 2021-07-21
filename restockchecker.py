## Sign inro site with the product
## Find product under X amount
## If the product is not available, wait until it is available
## Add product to cart


#Simple assignment
import selenium
from selenium.webdriver import Chrome

with Chrome() as driver:
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.support import expected_conditions as EC
    import time
    from random import randint

    driver = webdriver.Chrome(r'C:\Drivers\chromedriver.exe')

    AMAZON_TEST_URL = 'https://www.amazon.com/dp/B096LZFF6Z/ref=pe_825000_114212990_TE_FOCE_n_id'
    AMAZON_URL = 'https://www.amazon.com/PlayStation-5-Console/dp/B08FC5L3RG/ref=sr_1_1?dchild=1&keywords=playstation+5&qid=1605750925&rnid=2941120011&s=videogames&sr=1-1'
    # let x be the delay time taken to simulate real human
    x = 5

    class restockchecker:
        def __init__(self, username, password):
            """ Initializes Bot with class-wide variables. """
            self.username = username
            self.password = password
            self.driver = webdriver.Chrome()
        
        ## Sign into site with the product
        def signIn(self):
            """ Sign into site with the product. """
            driver = self.driver ## Navigate to URL
            
            ## Enter Username
            username_elem = driver.find_element_by_xpath("//input[@name='email']")
            username_elem.clear()
            username_elem.send_keys(self.username)
            
            time.sleep(randint(int(x/2), x))
            username_elem.send_keys(Keys.ENTER)
            time.sleep(randint(int(x/2), x))
            
            ## Enter Password
            password_elem = driver.find_element_by_xpath("//input[@name='password']")
            password_elem.clear()
            password_elem.send_keys(self.password)
            
            time.sleep(randint(int(x/2), x))
            password_elem.send_keys(Keys.ENTER)
            time.sleep(randint(int(x/2), x))
            
        ## Find product under X amount
        def findProduct(self):
            """ Finds the product with global link. """
            driver = self.driver
            driver.get(AMAZON_URL)
            time.sleep(randint(int(x/2), x))
            
            ## If the product is not available, wait until it is available
            isAvailable = self.isProductAvailable()
            PRICE_LIMIT = 10
            if isAvailable == 'Currently unavailable.':
                time.sleep(randint(int(x/2), x))
                self.findProduct()
            elif isAvailable <= PRICE_LIMIT:
                ## Buy Now
                buy_now = driver.find_element_by_name('submit.buy-now')
                buy_now.click()
                time.sleep(randint(int(x/2), x))
                self.signIn()
                time.sleep(randint(int(x/2), x))
                
                ## Place Order
                place_order = driver.find_element_by_xpath('//*[@id="placeYourOrder"]/span/input')
                time.sleep(randint(int(x/2), x))
                print(f'***** PLACE ORDER: {place_order}')
                time.sleep(randint(int(x/2), x))
                place_order.click()
                time.sleep(randint(int(x/2), x))
                
            else:
                time.sleep(randint(int(x/2), x))
                self.findProduct()
                
        def isProductAvailable(self):
            """ Checks if product is available. """
            driver = self.driver
            available = driver.find_element_by_class_name('a-color-price').text
            if available == 'Currently unavailable.':
                print(f'***** AVAILABLE: {available}')
                return available
            else:
                print(f'***** PRICE: {available}')
                return float(available[1:]) ## $123.22 -> 123.22
        
        def closeBrowser(self):
            """ Closes browser """
            self.driver.close()
            

    if __name__ == '__main__':
        shopBot = restockchecker(username="Email", password="Password")
        shopBot.findProduct()
        shopBot.closeBrowser()