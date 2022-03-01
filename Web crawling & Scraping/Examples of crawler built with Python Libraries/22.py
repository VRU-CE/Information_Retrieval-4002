from lxml import html
import requests


class AppCrawler:

    def __init__(self, starting_url, depth):
        self.starting_url = starting_url
        self.depth = depth
        self.apps = []
        
        
        
    def get_app_from_link(self, link):
             start_page = requests.get(link) 
             tree=html.fromstring(start_page.text) 
             name=tree.xpath('//h1[@itemprop="name"]/text()') 
             print(name)
             
             return    

    def crawl(self):
         self.get_app_from_link(self.starting_url)
         return
         
           
         
         


class App:

    def __init__(self, name, developer, price, links):
        self.name = name
        self.developer = developer
        self.price = price
        self.links = links

    def __str__(self):
        return ("Name: " + self.name.encode('UTF-8') + 
        "\r\nDeveloper: " + self.developer.encode('UTF-8') + 
        "\r\nPrice: " + self.price.encode('UTF-8') + "\r\n")


crawler = AppCrawler('https://itunes.apple.com/us/app/candy-crush-saga/id553834731', 2)
crawler.crawl()

for app in crawler.apps:
    print(app)