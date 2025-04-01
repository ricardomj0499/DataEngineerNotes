import urllib.request
from http.client import HTTPResponse  # Only for type hinting

spark_docs = "https://spark.apache.org/docs/latest/configuration.html"  # URL of the page to be scraped

page: HTTPResponse = urllib.request.urlopen(spark_docs)

### SOME FUNCTIONS OF HTTPRESPONSE OBJECT ###

# print(page) # <http.client.HTTPResponse object at 0x7f29fa3477f0>
# print(page.info()) # info() method returns the meta information of the page
# print(page.status) # status 200
# print(page.read()) # read() method returns the content of the page
# print(page.readline()) # b'\n'
# print(page.readline()) # b'<!DOCTYPE html>\n'
# print(page.readlines())
# print(page.getheaders()) same as info() method basically

# import the Beautiful soup functions to parse the data returned from the website
from bs4 import BeautifulSoup

soup = BeautifulSoup(
    page, "html.parser"
)  # This may be the name of a specific parser ("lxml","lxml-xml", "html.parser", or "html5lib") or it may be the type of markup to be used ("html", "html5", "xml").

### SOME FUNCTIONS OF BEAUTIFULSOUP OBJECT ###

# print(soup.prettify())
# print(soup.title) # <title>Configuration - Spark 3.5.4 Documentation</title>
# print(soup.title.string) # Configuration - Spark 3.5.4 Documentation
# print(soup.a) # <img height="72" src="img/spark-logo-rev.svg" width="141"/></a>

### FINDING ALL THE LINKS IN THE PAGE AND SOME UTITLY###
# all_links = soup.find_all("a")

# print(all_links)
# print("Total number of URLs present = ", len(all_links))
# print("\n\nLast 5 URLs in the page are : \n")
"""
if len(all_links) > 5:

    last_5 = all_links[len(all_links) - 5 :]
    for url in last_5:
        print(url.get("href"))
"""

### FINDING ALL THE TABLES IN THE PAGE ###
# all_tables = soup.find_all("table")
"""
for table in all_tables:
    print(table.name)
    print(table.attribute_value_list_class)
    print(table.attrs)
    print("-------------")
"""

# WE WANNA FIND THE APPLICATION PROPERTES TABLE, AS IT DOES NOT HAVE ANY CLASS OR ID, WE WILL HAVE TO FIND IT BY
# THE PREVIOUS ELEMENTS AND THEN GET NEXT SIBLING

title = soup.find("h3", attrs={"id": "application-properties"})  # .findNextSibling()
# print(title) # <h3 id="application-properties">Application Properties</h3>

table = title.find_next_sibling()
# print(table.contents) # [<thead>...</thead>, <tbody>...</tbody>]

head = table.find("thead")
# print(head) # <thead>...</thead>

head_headers = [
    x.text for x in head.find_all("th")
]  # ['Property Name', 'Default', 'Meaning']
# print("Head headers >", head_headers)

table_content = head.find_next_siblings()
# print(table_content) # THIS DOES NOT RETURN THE TBODY ELEMENT, SO IT GIVE UD DIRECTLY ALL THE
# ROWS OF THE TABLE, SO WE CAN ITERATE OVER IT AND GET THE DATA

df = []
for row in table_content:
    row_data = []
    cols = row.find_all("td")
    row_data.append(cols[0].text)
    row_data.append(cols[1].text)
    row_data.append(cols[2].text)
    row_data.append(cols[3].text)
    df.append(row_data)

import pandas as pd

# convert the list of lists into a pandas DataFrame
df = pd.DataFrame(df, columns=head_headers)

# print(df)

# WE THEN WRITE THE DATAFRAME TO A CSV FILE
df.to_csv("spark_application_properties.csv", index=True)

"""
# You can also use the pandas library to read the table directly from the URL. Here is an example:
import pandas as pd

# URL of the page containing the table
url = "https://spark.apache.org/docs/latest/configuration.html"

# Read all tables from the URL
tables = pd.read_html(url)

# Assuming the table you want is the first one
df = tables[0]

# Display the DataFrame
print(df)

# Save the DataFrame to a CSV file
df.to_csv("spark_application_properties_direct.csv", index=False)
"""

"""
# You can also use regex to read the table using re library. Here is an example:
import urllib.request
import re
import pandas as pd

# URL of the page containing the table
url = "https://spark.apache.org/docs/latest/configuration.html"

# Fetch the page content
response = urllib.request.urlopen(url)
html = response.read().decode('utf-8')

# Define a regex pattern to extract the table
table_pattern = re.compile(r'<table.*?>(.*?)</table>', re.DOTALL)
tables = table_pattern.findall(html)

# Assuming the table you want is the first one
table_html = tables[0]

# Extract table headers
header_pattern = re.compile(r'<th.*?>(.*?)</th>', re.DOTALL)
headers = header_pattern.findall(table_html)

# Extract table rows
row_pattern = re.compile(r'<tr.*?>(.*?)</tr>', re.DOTALL)
rows = row_pattern.findall(table_html)

# Extract table data
data = []
for row in rows:
    cell_pattern = re.compile(r'<td.*?>(.*?)</td>', re.DOTALL)
    cells = cell_pattern.findall(row)
    if cells:
        data.append([re.sub(r'<.*?>', '', cell) for cell in cells])

# Create DataFrame
df = pd.DataFrame(data, columns=headers)

# Display the DataFrame
print(df)

# Save the DataFrame to a CSV file
df.to_csv("spark_application_properties_regex.csv", index=False)

"""

# TODO:
# 1. Add pagination handling to scrape multiple pages.
# 2. Work with dynamic pages using Selenium or Scrapy.
# 3. Handle JavaScript-rendered content.
# 4. Implement error handling and retries for robust scraping.
# 5. Extract additional data elements as needed.
