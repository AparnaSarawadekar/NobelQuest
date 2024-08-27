import scrapy
import requests
import base64
from bs4 import BeautifulSoup

class WikispiderSpider(scrapy.Spider):
    name = "nwdcspider"
    allowed_domains = ["en.wikipedia.org"]
    start_urls = ["https://en.wikipedia.org/wiki/List_of_Nobel_laureates"]

    def image_encoder(self, url):
        try:
            response = requests.get("https:"+url)
            return base64.b64encode(response.content).decode("utf-8")
        except Exception as e:
            return None
    

    def parse(self, response):
        scientists = response.css(".fn")
        for scientist in scientists:
            yield response.follow("https://en.wikipedia.org/"+scientist.css("a::attr(href)").get(), callback=self.parse_scientist_page)

    def parse_scientist_page(self, response):
        pages = response.css(".mw-parser-output a")
        # print(response.url, ":", len(pages))
        for page in pages:
            page_url = page.css("::attr(href)").get()
            if "wiki" in page_url:
                yield response.follow("https://en.wikipedia.org/"+page_url, callback=self.scrape_page)

    def scrape_page(self, response):
        raw_text = response.css(".mw-content-ltr").extract()
        image = response.css(".mw-default-size img::attr(src)").get()
        yield {
            'Name': response.css(".mw-page-title-main::text").get(),
            'URL': response.url,
            'Data': BeautifulSoup(raw_text[0]).text.replace("\n","").replace('"',''),
            'Image_Serialized': self.image_encoder(image)
        }

