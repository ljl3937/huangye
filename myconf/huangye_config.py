# Code based on Python 3.x
# _*_ coding: utf-8 _*_
# __Author: "LEMON"

TOTAL_PAGE_NUMBER = 90  # PAGE_NUMBER: total number of pages，可进行修改

#KEYWORDS = ['大数据', 'python', '投资经理'] # 需爬取的关键字可以自己添加或修改
KEYWORDS = ['物流']

# 爬取主要城市的记录
# ADDRESS = ['全国', '北京', '上海', '广州', '深圳',
#            '天津', '武汉', '西安', '成都', '大连',
#            '长春', '沈阳', '南京', '济南', '青岛',
#            '杭州', '苏州', '无锡', '宁波', '重庆',
#            '郑州', '长沙', '福州', '厦门', '哈尔滨',
#            '石家庄', '合肥', '惠州', '太原', '昆明',
#            '烟台', '佛山', '南昌', '贵阳', '南宁']
ADDRESS = ['北京']

HOMEURL = 'http://www.9928.tv/company'

TYPES = {
	'jiudian': 'http://b2b.huangye88.com/qiye/jiudian/',
	'lingshi': 'http://b2b.huangye88.com/qiye/lingshi/',
	}

MONGO_URI = 'mongodb://172.16.100.2:32178'
MONGO_DB = 'huangye'