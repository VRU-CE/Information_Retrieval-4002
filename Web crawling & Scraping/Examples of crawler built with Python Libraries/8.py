from lxml import html
import requests


class AppCrawler(object):

    def __init__(self, starting_url, depth):
        self.starting_url = starting_url
                
        
    def get_app_from_link(self, link):
             start_page = requests.get(link) 
             tree=html.fromstring(start_page.text)
             #name=tree.xpath('//h1[@itemprop="name"]/text()') 
             name=tree.xpath('//*[@id="ember250"]/div/div[2]/header/h1')
             developer = tree.xpath('//*[@id="ember250"]/div/div[2]/header/h2[2]')
             price = tree.xpath('//*[@id="ember250"]/div/div[2]/header/ul[2]/li')
             links = tree.xpath('//div[@class="center-stack"]//*/a[@class="name"]/@href')
             print(name)
             print(developer)
             print(price)
             print(links)
             
            
             return    

    def crawl(self):
         self.get_app_from_link(self.starting_url)
         return
         
                 
         


crawler = AppCrawler('https://itunes.apple.com/us/app/subway-surfers/id512939461?mt=8', 2)
crawler.crawl()

