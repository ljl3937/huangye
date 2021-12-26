# Code based on Python 3.x
# _*_ coding: utf-8 _*_
# __Author: "LEMON"
import re
from multiprocessing import Pool
import requests
from bs4 import BeautifulSoup
# import pymongo

from myconf.meijiu_config import *
import time
import codecs
from xpinyin import Pinyin


def download(url):
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'}
    response = requests.get(url, headers=headers)
    return response.text


def getCityURL():
    html = download("http://www.9928.tv/company")
    soup = BeautifulSoup(html, 'lxml')
    body = soup.body
    urls = []
    for pro in ADDRESS:
        data_main = body.find_all('a',text=pro)
        for a in data_main:
            hr = a['href']
            if 'http' not in hr:
                url = 'http://www.9928.tv' + hr
                tmp = (a.text, url)
                urls.append(tmp)
    return urls

def getTels(city_url, path):
    base_url = city_url[1]
    type = city_url[0]
    time.sleep(3)
    tels = []
    pn = 1
    f = codecs.open(path, 'a', 'utf8')
    while pn > 0:
        url = base_url + str(pn)
        print(url)
        html = download(url)
        if html:
            print('正在爬取' + type + '第' + str(pn) + '页')
            soup = BeautifulSoup(html, 'lxml')
            body = soup.body
            pagerTitles = body.find_all('td', {'class': 'pagerTitle'})
            total_page = 1
            for pt in pagerTitles:
                if '共' in pt.get_text():
                    total_page = int(pt.get_text().split('共')[1].split('页')[0])
            print(total_page)
            data_main = body.find('div', {'class': 'qyk_css08'})
            if data_main:
                qys = data_main.find_all('div', {'class':'qy_div'})
                for qy in qys:
                    try:
                        name = qy.find('b').find('a').get_text().replace('\n', '').replace('\r', '')
                        url_str = qy.find('b').find('a').get('href')
                        url1 = 'http://www.9928.tv' + url_str
                        print(url1)
                        html1 = download(url1)
                        tel = ''
                        # infos = []
                        if html1:
                            soup1 = BeautifulSoup(html1, 'lxml')
                            body1 = soup1.body
                            tel_el = body1.find("div", class_="quick_nav").find("p", class_="nav_c")
                            tel = tel_el.get_text().strip().replace('\n', '').replace('\r', '').replace('预约回电>>', '')
                        info = "%s %s" % (name,tel)
                        # infos.append(info)
                        if '留言后企业回电给您' not in info:
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
            if pn == total_page:
                break
            pn += 1
    f.close()


def getItemURL(base_url):
    time.sleep(2)
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

def main():
    p = Pinyin()
    urls = getCityURL()
    # mongo_table = db['beijing']
    # path = '/run/media/jialin/Seagate/work/data/'
    path = '/home/jialin/code/huangye/data/'
    # print(urls)
    for url in urls:
        title = url[0]
        if "河南" not in title and "北京" not in title and "山东" not in title:
            getTels(url, path+p.get_pinyin(title, ''))


if __name__ == '__main__':
    start = time.time()
    # number_list = list(range(TOTAL_PAGE_NUMBER))
    # args = product(ADDRESS, number_list)
    # for arg in args:
    #     print(arg)
    args = ['jiudian', 'lingshi']
    # pool = Pool()
    # pool.map(main, args)  # 多进程运行
    main()
    end = time.time()
    print('Finished, task runs %s seconds.' % (end - start))
