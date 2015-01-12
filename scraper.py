# -*- coding: utf-8 -*-

# EDIT
from datetime import date
import json

from datetime import date
from bs4 import BeautifulSoup
import requests
import turbotlib

# present registered banks 
# source_url = "http://www.rbnz.govt.nz/regulation_and_supervision/banks/register/"
# list of past and present registered banks 
source_url = "http://www.rbnz.govt.nz/regulation_and_supervision/banks/0029134.html"
sample_date = str(date.today())
turbotlib.log("Starting scrape...") # optional debug logging
response = requests.get(source_url)
html = response.content
doc = BeautifulSoup(html)

# grab the html source if needed 
# print(doc.prettify())

table = doc.find('div', class_='band main')

# the first table row contains the column headings
# "Name of registered bank" and "Registration date"
# which we need to ignore as we want the data following them
first_tr = table.find('tr')

# the data is in all the siblings after the column headings
for tr in first_tr.find_next_siblings('tr'):
    # Each tr element has two td elements.
    tds = tr.find_all('td')
    record = {
        'bank_name': tds[0].text,
        'registration_date': tds[1].text,
        'sample_date': sample_date,   # mandatory field
        'source_url': source_url      # mandatory field
    }
    # The important part of the Turbot specification is that your scraper outputs lines of JSON
    print json.dumps(record)
