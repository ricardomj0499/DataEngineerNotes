# Bookstore Scraper

## Project Overview

This project is a web scraping tool built with Scrapy to extract book data from an online library. The goal is to periodically collect book information, store it, and analyze trends over time using DuckDB. This project was also an opportunity to re-learn Python while gaining hands-on experience with web scraping.

## Features

- Scrape books from an online library.
- Search for books by a specific author (e.g., Brandon Sanderson). (TODO)
- Traverse all pages recursively to collect book data. (TODO)
- Store extracted data in **Parquet** format for efficient storage and analysis. (TODO)
- Automate periodic data collection to track historical changes. (TODO)
- Perform basic data analysis using **DuckDB**.
- Run the scraper inside a **Jupyter Notebook**.
- Add datetime to data csv (Todo)

## Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/yourusername/bookstore_scraper.git
   cd bookstore_scraper
   ```
2. **Create a virtual environment and activate it:**
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

## Running the Scraper

To execute the scraper, use the following command:
```sh
scrapy runspider bookstore_scraper/spiders/bookstore_spider.py -O "books_%(time)s.csv"
```

## Storing Data

The scraped data is saved in various formats:
- **CSV** (default output format)
- **Parquet** (optimized for analytical processing)
- **DuckDB** (for efficient querying)

## To-Do List

- [ ] Implement search functionality for different authors.
- [ ] Enhance pagination handling to ensure all books are scraped.
- [ ] Store data in Parquet format.
- [ ] Automate periodic runs using a scheduler.
- [ ] Perform basic trend analysis on collected data.

## Useful Links & Documentation

- [Starting JupyterLab](https://jupyterlab.readthedocs.io/en/stable/getting_started/starting.html)
- [Scrapy Exporting Data](https://docs.scrapy.org/en/latest/topics/feed-exports.html)
- [Scrapy Pipelines](https://docs.scrapy.org/en/latest/topics/item-pipeline.html)
- [DuckDB Parquet Handling](https://duckdb.org/docs/stable/data/parquet/overview)
- [Scrapy Commands](https://docs.scrapy.org/en/latest/topics/commands.html)
- [Web Scraping with Scrapy](https://www.dataquest.io/blog/web-scraping-with-scrapy/)
- [Apache Arrow Parquet Docs](https://arrow.apache.org/docs/python/parquet.html)
