import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    start_urls = [
        'https://quotes.toscrape.com/page/1/',
        #'https://quotes.toscrape.com/page/2/',
    ]         

    def parse(self, response):
        quos = response.css('div.quote')
        qulist = []
        

        for qu in quos:
            qudict = {}
            qudict['text'] = qu.css("span.text::text").get()
            qudict['author'] = qu.css("small::text").get()
            qudict['about'] = qu.css("span a::attr(href)").get()
            qudict['tags'] = qu.css("div.tags a::attr(href)").getall()
            #qulist.append(qudict)
            yield qudict
            yield response.follow(qudict['about'], callback=self.parse_author)
        next_page = response.css('li.next a::attr(href)').get()

        if next_page is not None:
            #next_page = response.urljoin(next_page)
            yield response.follow(next_page, callback=self.parse)


        self.log(qulist)

    def parse_author(self, response):
        def extract_with_css(query):
            return response.css(query).get(default='').strip()

        yield {
            'name': extract_with_css('h3.author-title::text'),
            'birthdate': extract_with_css('.author-born-date::text'),
            'bio': extract_with_css('.author-description::text'),
        }