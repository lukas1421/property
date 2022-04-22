from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re
import pandas as pd

url = 'https://finviz.com/quote.ashx?t=' + comp + '&p=m&tas=0'
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
soup = BeautifulSoup(webpage, "html.parser")

url = 'https://hk.centanet.com/findproperty/list/transaction?q=e3CSEC7eUPrFVi8Vi6pg'
soup.find(text="實").parent.findNext('span').contents[0]
soup.find(attrs={'class': 'title-lg'}).parent.findNext('span').contents[0]

for x in soup.find_all('div',{'class':'right-block row-cxt'}):
    for y in x.find_all('span'):
        print('y is ', y)

for x in soup.find_all('div',{'class':'right-block row-cxt'}):
    print('x-----------------')
    for y in x.find_all('span'):
        if(y.text=='實'):
            print('next', '1', y.findNextSibling().text,'3', y.find_next_sibling().text)