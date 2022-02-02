from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re

req = Request("http://example.webscraping.com//")
html_page = urlopen(req)

soup = BeautifulSoup(html_page, "lxml")
#print(soup)

links = []
for link in soup.findAll('a'):
    links.append(link.get('href'))

#print(links)


#SCRIPT TO EXPORT IN EXCEL USING PANDAS


import numpy as np
import pandas as pd

df1 = pd.DataFrame({
    'Col A': [links],
})

df1.to_excel('df1.xlsx', index=False) # para que no aparezca el index