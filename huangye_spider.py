# Code based on Python 3.x
# _*_ coding: utf-8 _*_
# __Author: "LEMON"

from datetime import datetime
from urllib.parse import urlencode
from multiprocessing import Pool
import requests
from bs4 import BeautifulSoup
import pymongo
from huangye.huangye_config import *
import time
from itertools import product
import codecs

client = pymongo.MongoClient(MONGO_URI)
db = client[MONGO_DB]


def download(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0'}
    response = requests.get(url, headers=headers)
    return response.text

def getTels(base_url,type,path):
    tels = []
    pn =1
    f = codecs.open(path, 'a', 'utf8')
    while pn>0:
        url = base_url +'pn'+ str(pn)
        html = download(url)
        if html:
            print('正在爬取'+type+'第'+str(pn)+'页')
            soup = BeautifulSoup(html, 'lxml')
            body = soup.body
            data_main = body.find('form', {'name': 'jubao'})
            if data_main:
                dls = data_main.find_all('dl')
                for dl in dls:
                    try:
                        tel = dl.find('span').find('a').get_text()
                        tels.append(tel)
                        f.write(str(tel))
                        f.write('\n')
                    except:
                        pass
            try:
                pages = body.find('div', {'class':'page_tag Baidu_paging_indicator'}).find_all('a')
                texts = []
                for page in pages:
                    texts.append(page.get_text())
                if '下一页' not in texts:
                    print('最后一页')
                    pn = -3
                    return tels
            except:
                pass
            pn +=1
    f.close()

def getItemURL(base_url):
    html = download(base_url)
    soup = BeautifulSoup(html, 'lxml')
    body = soup.body
    data_main = body.find('div', {'class': 'ad_list'})
    urls = []
    if data_main:
        links = data_main.find_all('a')
        for link_info in links:
            link = link_info['href']
            title = link_info['title']
            urls.append({title:link})
    return urls


def main(args):
    urls = getItemURL(TYPES[args])
    mongo_table = db[args]
    path = '/home/jialin/Documents/hy/' + args
    # print(urls)
    for url in urls:  
        for title in url:
            tels = getTels(url[title],title,path)
            for tel in tels:                
                if mongo_table.update({'province':title},{'tel':tel},True):
                    print('已保存记录：', title,tel)

if __name__ == '__main__':
    start = time.time()
    # number_list = list(range(TOTAL_PAGE_NUMBER))
    # args = product(ADDRESS, number_list)
    # print(args[0])
    args =['母婴',]
    pool = Pool()
    pool.map(main, args) # 多进程运行
    end = time.time()
    print('Finished, task runs %s seconds.' % (end - start))