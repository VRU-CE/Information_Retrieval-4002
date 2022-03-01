from urllib.request import urlopen
from bs4 import BeautifulSoup
html=urlopen("http://www.imdb.com/news/top")
imdbNews=BeautifulSoup(html)
for headline in imdbNews.findAll("h2"):
    print(headline.get_text())