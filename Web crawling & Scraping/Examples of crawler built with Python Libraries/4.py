from lxml import html
import requests
start_page = requests.get('http://www.entekhab.ir/fa/services/3') 
tree=html.fromstring(start_page.text) 
name=tree.xpath('//*[@class="title6"]/text()')
for n in name:
            print(n)
           

             



