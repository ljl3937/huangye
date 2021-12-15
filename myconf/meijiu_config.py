# Code based on Python 3.x
# _*_ coding: utf-8 _*_
# __Author: "LEMON"

TOTAL_PAGE_NUMBER = 90  # PAGE_NUMBER: total number of pages，可进行修改

KEYWORDS = ['物流']


# 爬取主要城市的记录
# ADDRESS = ['全国', '北京', '上海', '广州', '深圳',
#            '天津', '武汉', '西安', '成都', '大连',
#            '长春', '沈阳', '南京', '济南', '青岛',
#            '杭州', '苏州', '无锡', '宁波', '重庆',
#            '郑州', '长沙', '福州', '厦门', '哈尔滨',
#            '石家庄', '合肥', '惠州', '太原', '昆明',
#            '烟台', '佛山', '南昌', '贵阳', '南宁']
ADDRESS = [
    '北京', '天津',	 '山东', '河南', '河北', '内蒙', '山西', '江西', '四川', '重庆', '贵州', '云南', '上海', '江苏', '安徽', '浙江', '甘肃', '福建', '湖北', '湖南', '广东', '广西', '吉林', '辽宁', '黑龙江', '陕西', '西藏', '宁夏', '青海', '海南', '台湾', '香港', '澳门', '新疆'
]

TYPES = {
    'jiudian': 'http://b2b.huangye88.com/qiye/jiudian/',
    'lingshi': 'http://b2b.huangye88.com/qiye/lingshi/',
}

MONGO_URI = 'mongodb://172.16.100.2:32178'
MONGO_DB = 'huangye'
