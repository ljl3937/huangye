import re

import requests
from bs4 import BeautifulSoup

from huangye_spider import download, get_num

url = "http://nihao230523.b2b.huangye88.com/"
html = download(url)
soup = BeautifulSoup(html, 'lxml')
body = soup.body
tel = body.find("span", class_="secret")
data = tel.get_text()

res = requests.get(url)
bs64_str = re.findall("charset=utf-8;base64,(.*?)\"\)", res.text)[0]
a = get_num(bs64_str, data)
print(a)
