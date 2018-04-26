class AppCrawler:
    def __init__(self, startingURL, depth):
        self.startingURL = startingURL
        self.depth = depth

    def crawl(self):
        return
    def getAppFromLink(self, link):
        return

class Apps:
    def __init__(self, name, price, links):
        self.name = name
        self.price = price
        self.links = links
    def __str__(self):
        return ("Name: " + self.name.encode('UTF-8') +
        "\r\nPrice:" + self.price.encode('UTF-8') + "\r\n" )

