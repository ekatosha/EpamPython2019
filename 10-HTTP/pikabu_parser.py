import requests
from bs4 import BeautifulSoup
import pandas as pd

DEFAULT_HEADERS = {
    "User-Agent": "Mozilla/4.0 (compatible; MSIE 7.0;\ Windows NT 6.0)",
    "Referer": "http://pikabu.ru/",
    "Host": "pikabu.ru",
    "Origin": "pikabu.ru"
}

with open('C:/Users/ekant/Desktop/cookies.txt') as f:
        DEFAULT_HEADERS['Cookie'] = f.read()
s = requests.Session()
pages = ''
for i in range(1,10):
    resp = s.get(f'https://pikabu.ru/hot/subs/actual?page={i}', headers=DEFAULT_HEADERS)
    pages += resp.text
soup = BeautifulSoup(pages,'html.parser')
application = soup.find_all('a', {'data-tag' : True})
tag_list = {}
for string in application:
    if string.get_text() in tag_list:
        tag_list[string.get_text()] += 1
    else:
        tag_list[string.get_text()] = 1
df = pd.DataFrame.from_dict(tag_list, orient='index', columns = ['quantity'])
print(df.sort_values(by=['quantity'], ascending = False)[:10])

#без cookies
""""
DEFAULT_HEADERS = {
    "User-Agent": "Mozilla/4.0 (compatible; MSIE 7.0;\ Windows NT 6.0)",
    "Referer": "http://pikabu.ru/",
    "Host": "pikabu.ru",
    "Origin": "pikabu.ru"
}
tag_list = {}
s = requests.Session()
pages = ''
for i in range(1,10):
    resp = s.get(f'https://pikabu.ru/hot/actual', headers=DEFAULT_HEADERS)
    pages += resp.text
soup = BeautifulSoup(response.text,'html.parser')
application = soup.find_all('a', {'data-tag' : True})
for string in application:
    if string.get_text() in tag_list:
        tag_list[string.get_text()] += 1
    else:
        tag_list[string.get_text()] = 1
df = pd.DataFrame.from_dict(tag_list, orient='index', columns = ['quantity'])
print(df.sort_values(by=['quantity'], ascending = False)[:10]) """