from lxml import html
import requests
import csv
f=csv.writer(open("./asli9.csv","a+",encoding='utf-8'))
f.writerow(["my data"])

class AppCrawler:

    def __init__(self, starting_url, depth):
        self.starting_url = starting_url
        self.depth = depth
        self.current_depth = 0
        self.depth_links = []
        self.apps = []

    def crawl(self):
        app = self.get_app_from_link(self.starting_url)
        self.apps.append(app)
        self.depth_links.append(app.links)

        while self.current_depth < self.depth:
            current_links = []
            for link in self.depth_links[self.current_depth]:
                current_app = self.get_app_from_link(link)
                current_links.extend(current_app.links)
                self.apps.append(current_app)
                
            self.current_depth += 1
            self.depth_links.append(current_links)


    def get_app_from_link(self, link):
        start_page = requests.get(link)
        tree = html.fromstring(start_page.text)

        name = tree.xpath('//*[@class="title6"]/text()')
          
        
        for n in name:
            print(n)
            f.writerow([n])
       
        links =tree.xpath('//*[@class="pager_ax"]/a/@href')     
        link1=[]
        for t in links:
            link1.append('http://www.entekhab.ir'+t)
        
        app = App(name,link1)

        return app


class App:

    def __init__(self,name,links):
        self.name = name
        self.links = links

   

crawler = AppCrawler('http://www.entekhab.ir/fa/services/3', 2)
crawler.crawl()

f=csv.writer(open("./asli4.csv","a+",encoding='utf-8'))
f.writerow(["product Title"])

