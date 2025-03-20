import scrapy
from pathlib import Path
from scrapy.http.response.text import TextResponse


class LibrarySpider(scrapy.Spider):
    name = "LibrarySpider"

    def __init__(self):
        pass

    def start_requests(self):  # Could only set a list with the urls to scrap
        urls = [
            "https://www.libreriainternacional.com/catalogsearch/result/?q=brandon+sanderson",
            "https://www.libreriainternacional.com/catalogsearch/result/index/?p=2&q=brandon+sanderson",
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response: TextResponse):  # Scrapy’s default callback method
        page = response.url.split("/")[-2]
        filename = f"library-{page}.html"
        Path(filename).write_bytes(response.body)
        self.log(f"Saved file {filename}")
