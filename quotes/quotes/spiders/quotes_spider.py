# -*- coding: utf-8 -*-
import scrapy


class QuotesSpiderSpider(scrapy.Spider):
    name = 'quotes_spider'
    allowed_domains = ['http://quotes.toscrape.com/']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        all_div_quotes = response.css('div.quote')
        quotes = all_div_quotes.css('span.text::text').extract()
        author = all_div_quotes.css('.author::text').extract()
        tags = all_div_quotes.css('.tag::text').extract()
        yield {
            'quotes': quotes,
            'author': author,
            'tags': tags,
        }
