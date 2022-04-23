from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

url = 'https://hk.centanet.com/findproperty/list/transaction?q=e3CSEC7eUPrFVi8Vi6pg'
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
soup = BeautifulSoup(webpage, "html.parser")

# for x in soup.find_all('div',{'class':'right-block row-cxt'}):
#     for y in x.find_all('span'):
#         print('y is ', y)
#
# for x in soup.find_all('div',{'class':'right-block row-cxt'}):
#     print('x-----------------')
#     for y in x.find_all('span'):
#         if(y.text=='實'):
#             print('next', '1', y.findNextSibling().text,'3', y.find_next_sibling().text)
###
# for x in soup.find_all('div',{'class':'right-block row-cxt'}):
#     print('x-----------------')
#     print(x)

##
for x in soup.find_all('div', {'class': 'right-block row-cxt'}):
    print('x-----------------')

    for y in x.find_all('div', {'class': 'title'}):
        print('title', y.text.strip())

    for y in x.find_all('div', {'class': 'col-detail'}):
        print('detail', y.text.strip())

    # for y in x.find_all('div', {'class': 'num'}):
    #     print('num', y.text.strip())

    y = x.find('div', {'class': 'num'})
    z = y.find('span', {'class': 'hidden-xs-only'})
    z1 = y.find('div', {'class': 'area-price'})
    z2 = z1.find('span')
    print('z', z.text.strip())
    print('z2', z2.text.strip().split()[1])

    # for y in x.find_all('div', {'class': 'num'}):
    #     # print('y', y)
    #     print('find first', y.find('span', {'class': 'hidden-xs-only'}))
    #     # for z in y.find_all('span', {'class': 'hidden-xs-only'}):
    #     #     # print('num', z.text.strip())
    #     #     print('num', z)
    #
    #     for z in y.find_all('div', {'class': 'area-price'}):
    #         print('area price', z.text.strip())

    # for y in x.find_all('div', {'class': 'area-price'}):
    #     print('area price', y.text.strip())

    for y in x.find_all('div', {'class': 'date'}):
        print('date', y.text.strip())

    for y in x.find_all('div', {'class': 'price'}):
        print('price', y.text.strip())
