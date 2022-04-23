import math
from bokeh.palettes import Dark2
from bokeh.plotting import show
import pandas as pd
from bokeh.models import ColumnDataSource, HoverTool
from bokeh.plotting import figure
from bokeh.transform import factor_cmap
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

pd.set_option('display.expand_frame_repr', False)
url = 'https://hk.centanet.com/findproperty/list/transaction?q=e3CSEC7eUPrFVi8Vi6pg'
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
soup = BeautifulSoup(webpage, "html.parser")

df = pd.DataFrame({'title': pd.Series(dtype='str'),
                   'location': pd.Series(dtype='str'),
                   'size': pd.Series(dtype='int'),
                   'pricePerSqft': pd.Series(dtype='int'),
                   'date': pd.Series(dtype='str'),
                   'totalPrice': pd.Series(dtype='int')})
##
for x in soup.find_all('div', {'class': 'right-block row-cxt'}):
    print('x-----------------')

    for y in x.find_all('div', {'class': 'title'}):
        title = y.text.strip().replace(' ', '_')
        print('title', title)

    for y in x.find_all('div', {'class': 'col-detail'}):
        location = y.text.strip().split()[0]
        print('location', location)

    y = x.find('div', {'class': 'num'})
    z = y.find('span', {'class': 'hidden-xs-only'})
    z1 = y.find('div', {'class': 'area-price'})
    z2 = z1.find('span')
    size = z.text.strip().split()[0]
    print('size', size)
    pricePerSqft = z2.text.strip().split()[1].replace('$', '')
    print('pricePerSqft', pricePerSqft)

    for y in x.find_all('div', {'class': 'date'}):
        date = y.text.strip()
        print('date', date)

    for y in x.find_all('div', {'class': 'price'}):
        totalPrice = y.text.strip().replace(',', '').replace('$', '').strip()
        print('price', totalPrice)

    df.loc[len(df.index)] = [title, location, size, pricePerSqft, date, totalPrice]

print(df)
df['pricePerSqft'] = df['pricePerSqft'].astype(int)
df = df.set_index('date')
df.index = pd.to_datetime(df.index)
df = df.sort_index()
df['level'] = df['title'].apply(lambda x: x.split('_')[2])
df['10ma'] = df['pricePerSqft'].rolling(10).mean()
df['5ma'] = df['pricePerSqft'].rolling(5).mean()
df['level'] = df['title'].apply(lambda x: x.split('_')[2])

global_source = ColumnDataSource(pd.DataFrame())
global_source.data = ColumnDataSource.from_df(df)

p = figure(title='prices chart', width=1000, x_axis_type="datetime")
p.xaxis.major_label_orientation = math.pi / 4
p.grid.grid_line_alpha = 0.3
p.add_tools(HoverTool(tooltips=[('date', '@date{%Y-%m-%d}'), ('pricePerSqft', '@pricePerSqft'),
                                ('level', '@level')], formatters={'@date': 'datetime'}, mode='mouse'))
pal = Dark2[3]
p.circle(x='date', y='pricePerSqft', source=global_source, size=15, legend='level',
         fill_color=factor_cmap('level', palette=pal, factors=df['level'].unique()))
p.legend.label_text_font_size = '20pt'

print(df)
show(p)
