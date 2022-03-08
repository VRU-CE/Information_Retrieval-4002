from lxml import html
import requests
import csv


f = csv.writer(open("./asli9.csv", "w", encoding='utf-8'))
f.writerow(["my data"])


class AppCrawler:

    def __init__(self, starting_url, depth):
        self.starting_url = starting_url
        self.depth = depth
        self.current_depth = 0
        self.depth_links = []
        self.apps = []

    def crawl(self):
        book = self.get_app_from_link(self.starting_url)
        self.apps.append(book)
        # self.depth_links.append(app.links)

        # while self.current_depth < self.depth:
        #     current_links = []
        #     for link in self.depth_links[self.current_depth]:
        #         current_app = self.get_app_from_link(link)
        #         current_links.extend(current_app.links)
        #         self.apps.append(current_app)

        # self.current_depth += 1
        # self.depth_links.append(current_links)

    def get_app_from_link(self, link):
        start_page = requests.get(link)
        tree = html.fromstring(start_page.text)

        description = tree.xpath(
            '''//p[contains(text(),"It's hard to imagine a world without A Light in th")]/text()''')[0]

        price = tree.xpath("//p[@class='price_color']/text()")[0]
        name = tree.xpath(
            "//h1[normalize-space()='A Light in the Attic']/text()")[0]

        f.writerow([name, price, description])

        # links = tree.xpath('//*[@class="pager_ax"]/a/@href')
        # link1 = []
        # for t in links:
        #     link1.append('http://www.entekhab.ir'+t)

        book = Book(name, price, description)

        return book


class Book:

    def __init__(self, name, price, description):

        self.name = name
        self.price = price
        self.description = description
        # self.links = links


crawler = AppCrawler(
    'https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html', 2)
crawler.crawl()

# f = csv.writer(open("./asli4.csv", "w", encoding='utf-8'))
# f.writerow(["product Title"])
