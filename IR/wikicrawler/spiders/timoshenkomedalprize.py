import scrapy
import requests
import base64
from bs4 import BeautifulSoup

class WikispiderSpider(scrapy.Spider):
    name = "tmspider"
    allowed_domains = ["en.wikipedia.org"]
    start_urls = ["https://en.wikipedia.org/wiki/Timoshenko_Medal"]

    def image_encoder(self, url):
        try:
            response = requests.get("https:"+url)
            return base64.b64encode(response.content).decode("utf-8")
        except Exception as e:
            return None
    
    def parse(self, response):
        entries = response.css(".mw-parser-output ul li a::attr(href)").getall()   
        for entry in entries:
            yield response.follow("https://en.wikipedia.org/"+entry, callback=self.scrape_scientist_page)

    def scrape_scientist_page(self, response):
        raw_text = response.css(".mw-content-ltr").extract()
        image = response.css(".mw-default-size img::attr(src)").get()
        yield {
            'Name': response.css(".mw-page-title-main::text").get(),
            'URL': response.url,
            'Data': BeautifulSoup(raw_text[0]).text.replace("\n","").replace('"',''),
            'Image_Serialized': self.image_encoder(image)
        }