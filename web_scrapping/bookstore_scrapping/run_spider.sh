#!/bin/bash

scrapy runspider /home/ricardo/data_engineer_notes/DataEngineerNotes/web_scrapping/bookstore_scrapping/bookstore_scraper/bookstore_scraper/spiders/bookstore_spider.py -O data/books_$(date +"%Y-%m-%d_%H-%M-%S" -u --date='6 hours ago').csv
