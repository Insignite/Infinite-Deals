import selenium.webdriver as webdriver
from bs4 import BeautifulSoup
import csv
import cgi

def get_link(search_term):
    # Make sure to move chrome driver to project folder
    chromeDriver = '/usr/local/bin/chromedriver'

    # Add options to chrome
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=1920x1080')

    # Website Links
    url = "https://www.bestbuy.com/"
    newegg_url = "https://www.newegg.com/?nm_mc=KNC-Askcom&cm_mmc=KNC-Askcom-_-Branding-_-NA-_-NA"

    # Selenium Setting chrome driver and access website
    browser = webdriver.Chrome(executable_path = chromeDriver, chrome_options = options)

    # Add options
    options = webdriver.ChromeOptions()

    options.add_argument('headless')

    # Get the url
    browser.get(newegg_url)

    # Find search bar input content
    search_bar = browser.find_element_by_id("haQuickSearchBox")

    # Pass in Search term and do a automatic search
    search_bar.send_keys(search_term)
    search_bar.submit()

    # Grabbing all HTML Code
    html_source = browser.page_source

    # Setting pass in text code as html code
    soup = BeautifulSoup(html_source, "html.parser")

    # List to store data
    products_info = []

    # Soup object searching through products containers
    container_box = soup.findAll("div", {"class" : "item-container"})

    # For loop to find name, price, and link through the container section
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

        # Add to product list
        products_info.append([UniTempName, FinalUniTempPrice, UniTempLink])

    # Create, open csv file
    with open('products.csv', 'wb') as myfile:
        wr = csv.writer(myfile, quoting = csv.QUOTE_ALL)
        # Write the header
        wr.writerow(("Name", "Price", "URL"))
        # List through the tuple and write to file
        for info in products_info:
            if(search_term.upper() in info[0].upper()):
                wr.writerow(info)
    # close the csv file
    myfile.close()

def __init__(self):
    HtmlFormSearch = cgi.FieldStorage()
    get_link(HtmlFormSearch.getvalue('search'))
