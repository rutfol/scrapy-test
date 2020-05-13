import scrapy
from scrapy.crawler import CrawlerProcess
import urllib.request as urllib2
import json
import urllib 

import re
import urllib.parse

class LinksSpider(scrapy.Spider) :
    name = "links"
    

    def start_requests(self):
        start_urls = [
            "https://www.snerpa.is/net/isl/isl-th.htm",
            "https://www.snerpa.is/net/snorri/heimskri.htm"
        ]
        for url in start_urls:
            yield scrapy.Request(url=url, callback=self.parse)


    def parse(self, response) :
        linksList = []
        for link in response.xpath("//a/@href"):
            if link.get().index("/") < 2:
                linksList.append("https://www.snerpa.is/net/isl" + link.get()[1:])
        yield {
            "links": linksList
        }
        
