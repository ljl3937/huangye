import base64
from io import BytesIO
from fontTools.ttLib import TTFont
import requests
import re
from lxml import etree


url = 'https://cd.58.com/wuhou/chuzu/b5j5'
res = requests.get(url)
bs64_str = re.findall("charset=utf-8;base64,(.*?)'\)", res.text)[0]


def get_page_show_ret(string):
    font = TTFont(BytesIO(base64.decodebytes(bs64_str.encode())))
    c = font['cmap'].tables[0].ttFont.tables['cmap'].tables[0].cmap
    ret_list = []
    for char in string:
        decode_num = ord(char)
        if decode_num in c:
            num = c[decode_num]
            num = int(num[-2:])-1
            ret_list.append(num)
        else:
            ret_list.append(char)
    ret_str_show = ''
    for num in ret_list:
        ret_str_show += str(num)
    return ret_str_show


page = etree.HTML(res.text)
li = page.xpath('.//ul[@class="listUl"]//li')[0:-1]
for each_li in li:
    title = each_li.xpath('.//div[@class="des"]/h2/a/text()')[0].strip()
    title = get_page_show_ret(title)
    price = each_li.xpath('.//div[@class="money"]/b/text()')[0]
    price = get_page_show_ret(price)
    print(title)
    print(price)
    print('='*20)