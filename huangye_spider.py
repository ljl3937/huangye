# Code based on Python 3.x
# _*_ coding: utf-8 _*_
# __Author: "LEMON"
import base64
import re
from datetime import datetime
from multiprocessing import Pool
import requests
from bs4 import BeautifulSoup
import pymongo
from fontTools.ttLib import TTFont, BytesIO

from myconf.huangye_config import *
import time
from itertools import product
import codecs

client = pymongo.MongoClient(MONGO_URI)
db = client[MONGO_DB]
map = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "zero": 0
}

def make_font_file(base64_string: str):
    bin_data = base64.decodebytes(base64_string.encode())
    with open('text.otf', 'wb') as f:
        f.write(bin_data)
    return bin_data
#
# font = TTFont(BytesIO(make_font_file(base64_str)))
# c = font['cmap'].tables[0].ttFont.tables['cmap'].tables[3].cmap


def get_num(bs64_str,string):
    font = TTFont(BytesIO(base64.decodebytes(bs64_str.encode())))
    c = font['cmap'].tables[0].ttFont.tables['cmap'].tables[3].cmap
    ret_list = []
    for char in string:
        decode_num = ord(char)
        c1 = c
        if decode_num in c1:
            num = c1[decode_num]
            num = map[num]
            ret_list.append(num)
        else:
            ret_list.append(char)
    ret_str_show = ''
    for num in ret_list:
        ret_str_show += str(num)
    return ret_str_show

def download(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0'}
    response = requests.get(url, headers=headers)
    return response.text


def getTels(base_url, type, path):
    tels = []
    pn = 1
    f = codecs.open(path, 'a', 'utf8')
    while pn > 0:
        url = base_url + 'pn' + str(pn)
        html = download(url)
        if html:
            print('正在爬取' + type + '第' + str(pn) + '页')
            soup = BeautifulSoup(html, 'lxml')
            body = soup.body
            data_main = body.find('form', {'name': 'jubao'})
            if data_main:
                dls = data_main.find_all('dl')
                for dl in dls:
                    try:
                        name = dl.find('h4').find('a').get_text()
                        url1 = dl.find('h4').find('a').get('href')
                        res = download(url1)
                        # res = requests.get(url1)
                        # bs64_str = re.findall("charset=utf-8;base64,(.*?)\"\)", res.text)[0]
                        bs64_str = re.findall("charset=utf-8;base64,(.*?)\"\)", res)[0]
                        html1 = download(url1)
                        tel = ''
                        # infos = []
                        if html1:
                            soup1 = BeautifulSoup(html1, 'lxml')
                            body1 = soup1.body
                            tel_el = body1.find("span", class_="secret")
                            tel_data = tel_el.get_text()
                            tel = get_num(bs64_str, tel_data)
                        info = "%s %s" % (name,tel)
                        # infos.append(info)
                        print(info)
                        f.write(str(info))
                        f.write('\n')
                        # break
                    except:
                        pass
            try:
                pages = body.find('div', {'class': 'page_tag Baidu_paging_indicator'}).find_all('a')
                texts = []
                for page in pages:
                    texts.append(page.get_text())
                if '下一页' not in texts:
                    print('最后一页')
                    pn = -3
                    f.close()
                    return tels
            except:
                pass
            pn += 1
    f.close()


def getItemURL(base_url):
    html = download(base_url)
    soup = BeautifulSoup(html, 'lxml')
    body = soup.body
    data_main = body.find_all('div', {'class': 'ad_list'})
    urls = []
    if data_main:
        links = data_main[1].find_all('a')
        for link_info in links:
            link = link_info['href']
            title = link_info['title']
            urls.append({title: link})
    return urls


def main(args):
    urls = getItemURL(TYPES[args])
    mongo_table = db[args]
    path = '/Users/lijialin/Documents/hy/' + args
    # print(urls)
    for url in urls:
        for title in url:
            if "北京" in title:
                tels = getTels(url[title], title, path)
                for tel in tels:
                    if mongo_table.update_one({'province': title}, {'tel': tel}, True):
                        print('已保存记录：', title, tel)


if __name__ == '__main__':
    start = time.time()
    # number_list = list(range(TOTAL_PAGE_NUMBER))
    # args = product(ADDRESS, number_list)
    # for arg in args:
    #     print(arg)
    args = ['物流', ]
    pool = Pool()
    pool.map(main, args)  # 多进程运行
    end = time.time()
    print('Finished, task runs %s seconds.' % (end - start))
