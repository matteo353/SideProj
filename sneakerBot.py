
import requests
import json
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time



#function checks the availibility of product and returns url if present on site
#Definitely returns correct url if given the right input
def productChecker(website, nameOfProduct):

    websitelink = 'https://www.' + website + '/products.json'
    productData = requests.get(websitelink)

    #products gives us all products listed on given site
    products = json.loads((productData.text))['products']
    url = 'https://www.' + website + '/products/'

    for item in products:
        if (item['title'] == nameOfProduct):
            itemLink = url + item['handle']
            print(itemLink)
            return itemLink

    return False
    


#pretty sure all shopify sites have the same backend syntax but have to check
#function to open url and checkout given shoe in selected size, ends at payment page
def checkoutBot(link, shoesize):

    #initializing web driver
    driver = webdriver.Chrome(ChromeDriverManager().install())

    #opening product page
    driver.get(link)

    #clicking on size of selected shoe
    sizeFormat = "'//div[@data-value=" + '"' + shoesize + '"' + "]'"
    print(sizeFormat)
    driver.find_element_by_xpath(sizeFormat).click()

    #clicking add to cart button and waiting for page to load
    driver.find_element_by_xpath('//button[@class="ffg productForm-submit js-productForm-submit"]').click()
    time.sleep(1)

    #clicking checkout button and waiting for page to load
    driver.find_element_by_xpath('//button[@class="button cart-checkout"]').click()
    time.sleep(1)

    #Filling in shipping info
    driver.find_element_by_xpath('//input[@placeholder="Email"]').send_keys("matteomastandrea1@gmail.com")
    driver.find_element_by_xpath('//input[@placeholder="First name"]').send_keys("Matteo")
    driver.find_element_by_xpath('//input[@placeholder="Last name"]').send_keys("Mastandrea")
    driver.find_element_by_xpath('//input[@placeholder="Address"]').send_keys("44 Example st")
    driver.find_element_by_xpath('//input[@placeholder="City"]').send_keys("Milton")
    driver.find_element_by_xpath('//input[@placeholder="ZIP code"]').send_keys("02186")

    #checking terms and conditions box
    driver.find_element_by_xpath('//input[@id="i-agree-terms__checkbox"]').click()

    #filling in phone number and hitting enter (the enter key: u'\ue007) / waiting for page to load
    driver.find_element_by_xpath('//input[@placeholder="Phone"]').send_keys("555-555-5555" + "\ue007")
    time.sleep(1)

    #clicking continue to payment button
    driver.find_element_by_xpath('//button[@class="step__footer__continue-btn btn"]').click()
    
    #ends at payment page


def functionManager(website, nameOfProduct, shoesize):
    if (productChecker(website, nameOfProduct) == False):
        print('Item not available')
        return
    else:
        link = productChecker(website, nameOfProduct)
        checkoutBot(link, shoesize)



#issue right now is that there is an error with selecting the size of the shoe, for some reason it doesn't like
#the call to select the value 12 even tho its the only one, code is outputting the right value tho
functionManager('shoepalace.com', 'Air Max 95 Raygun Mens Lifestyle Shoes (Black/Cosmic Clay/Kumquat/White)', '12'






# def shoeBot():
#     websiteName = input("website name: ")
#     prodName = input("name of product: ")
#     prodCategory = input("category of product: ")
#     prodColor = input("color: ")
#     shoeSize = input("shoe size: ")
#     fullName = prodName + ' ' + prodCategory + ' (' + prodColor + ')'
#     functionManager(websiteName, fullName, shoeSize)

shoeBot()

