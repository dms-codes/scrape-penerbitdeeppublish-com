import requests as r
import csv, time
from bs4 import BeautifulSoup as bs

HOME = 'https://deepublishstore.com/'
html = r.get(HOME).content
category_soup = bs(html,'html.parser')
category_urls = category_soup.find('ul', class_='mega-sub-menu').find_all('a', class_='mega-menu-link')
for category_url in category_urls:
    html = r.get(category_url['href']).content
    soup = bs(html,'html.parser')
    category_last_page = int(soup.find_all('a', class_='page-numbers')[-2].text)
    category_page_urls = []
    category_page_urls.append(HOME+'product-category/agama-islam/page/')
    for i in range(2,category_last_page+1):
        category_page_urls.append(f'{HOME}product-category/agama-islam/page/{i}')
    for category_page_url in category_page_urls:
        html= r.get(category_page_url).content
        soup = bs(html,'html.parser')
        
