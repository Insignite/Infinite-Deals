'''
This file is mean to use a test file to avoid damaging main code file.
Removing this file project has no effect to the project

'''

'''
import selenium.webdriver as webdriver
from bs4 import BeautifulSoup
import csv

def get_link(search_term):
    # Make sure to move chrome driver to project folder
    chromeDriver = '/usr/local/bin/chromedriver'

    # Website Links
    url = "https://www.bestbuy.com/"
    newegg_url = "https://www.newegg.com/?nm_mc=KNC-Askcom&cm_mmc=KNC-Askcom-_-Branding-_-NA-_-NA"

    # Selenium Setting chrome driver and access website
    browser = webdriver.Chrome(chromeDriver)
    browser.get(newegg_url)

    # Find search bar input content
    search_bar = browser.find_element_by_id("haQuickSearchBox")

    # Pass in Search term and do a automatic search
    search_bar.send_keys(search_term)
    search_bar.submit()

    # Creating a csv file and put settinf as w ( write )m should use a for setting
    #f = open("Products.csv", "w")

    # Grabbing all HTML Code
    html_source = browser.page_source

    # Setting pass in text code as html code
    soup = BeautifulSoup(html_source, "html.parser")

    #Create header for csv file
    headers = "product_name, price\n"
    #f.write("")

    # List to store data
    products_info = []

    # Soup object searching through products containers
    container_box = soup.findAll("div", {"class" : "item-container"})

    for contain in container_box:
        # Name section
        name_box = contain.find("a", {"class":"item-title"})
        UniTempName = name_box.text.encode('utf-8')

        # Link section
        UniTempLink = name_box.get('href').encode("utf-8")

        # Price section
        price_box = contain.find("li", {"class" : "price-current"})
        UniTempPrice = price_box.text.encode('utf-8').strip("\n-|")
        NewUniTempPrice = UniTempPrice.replace('\xc2\xa0\n', ' ').strip('\n\xe2\x80\x93').strip(' ')
        FinalUniTempPrice = NewUniTempPrice.replace('\xc2\xa0',' ').strip(' ')

        products_info.append([UniTempName, FinalUniTempPrice, UniTempLink])


    with open('products.csv', 'wb') as myfile:
        wr = csv.writer(myfile, quoting = csv.QUOTE_ALL)
        wr.writerow(("Name", "Price", "URL"))
        for info in products_info:
            if(search_term.upper() in info[0].upper()):
                wr.writerow(info)
    myfile.close()
    '''

    '''
    with open('products.csv', 'wb') as myfile:
        wr = csv.writer(myfile, quoting = csv.QUOTE_ALL)
        wr.writerow(("Name", "Price", "URL"))
        for key in productDictionary.keys():
            neweggs_name = key
            inputCSV_row = neweggs_name
            for value in productDictionary[key]:
                newsegg_price_url = value
                inputCSV_row = inputCSV_row + "," + value
            inputCSV_row = inputCSV_row + "\n"
            wr.writerow(inputCSV_row)
    myfile.close()

    '''
    # Creating a dictionary and bound the product name and price together

    '''
    print ("Name list size: ",len(name))
    print ("Price list size: ", len(price))
    print ("Link list size: ", len(link))
    print("--------------------")
    print(name)
    print ("--------------------")
    print price
    print("----------------------")
    print(link)
    print("----------------------")
    productDictionary = dict(zip(name,zip(price, link)))
    print productDictionary
    '''

get_link("alienware")
