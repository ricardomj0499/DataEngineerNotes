"""
This spider is used to scrap the libreria internacional website
"""

import scrapy
from scrapy.http.response.text import TextResponse
from bs4 import BeautifulSoup


class BookStoreSpider(scrapy.Spider):
    """
    This spider is used to scrap the libreria internacional website
    """

    name = "BookStoreSpider"

    def start_requests(
        self,
    ):
        # Could only set a list with the urls to scrap with list name = start_urls

        urls = [
            "https://www.libreriainternacional.com/catalogsearch/result/?q=BRANDON+SANDERSON",
        ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response: TextResponse):
        """
        Scrapy’s default callback method
        that will call another parse method for each book
        """
        list_books = response.css(".product-item-info")
        for book in list_books:
            book_url: str = book.css("a.product-item-link::attr(href)").get()
            if not book_url:
                continue
            yield scrapy.Request(book_url, self.parse_page)

        # Pagination handling: Find the 'Next' button and follow the link
        # We could use the next page link to scrap the next page
        # if the next page exists for example: ?p=2&q=brandon+sanderson"
        next_page = response.css(
            "a.action.next::attr(href)"
        ).get()  # Adjust selector if necessary
        if next_page:
            yield response.follow(next_page, callback=self.parse)

    def parse_page(self, response: TextResponse):
        """
        scrap every book that it finds using  beautifulsoup
        """

        page = BeautifulSoup(response.text, "html.parser")

        name = page.find("h1", {"class": "page-title"}).text.strip().replace("\n", "")
        author = page.find("a", class_="page-title-author").find("span").text  # none
        price = page.find("span", {"class": "price"}).text

        editorial = page.find("a", {"class": "page-title-editorial"}).text.replace(
            "\n", ""
        )
        publication_date = page.find("div", {"class": "attribute-publicacion"})
        publication_date = (
            publication_date.find("div", {"class": "attribute-value"}).text.strip()
            if publication_date
            else None
        )

        num_pages = page.find("div", {"class": "attribute-extension"})
        num_pages = (
            num_pages.find("div", {"class": "attribute-value"}).text
            if num_pages
            else None
        )

        language = page.find("div", {"class": "attribute-idioma"})
        language = (
            language.find("div", {"class": "attribute-value"}).text
            if language
            else None
        )

        lista_temas = []
        temas = (
            page.find("div", {"class": "attribute-tema"})
            .find("div", {"class": "attribute-value"})
            .find_all("a")
        )
        for x in temas:
            lista_temas.append(x.text.strip())

        return {
            "name": name,
            "author": author,
            "price": price,
            "editorial": editorial,
            "publication_date": publication_date,
            "num_pages": num_pages,
            "language": language,
            "lista_temas": lista_temas,
        }
