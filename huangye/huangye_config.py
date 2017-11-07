# Code based on Python 3.x
# _*_ coding: utf-8 _*_
# __Author: "LEMON"

TOTAL_PAGE_NUMBER = 90  # PAGE_NUMBER: total number of pages，可进行修改

#KEYWORDS = ['大数据', 'python', '投资经理'] # 需爬取的关键字可以自己添加或修改
KEYWORDS = ['视觉设计']

# 爬取主要城市的记录
# ADDRESS = ['全国', '北京', '上海', '广州', '深圳',
#            '天津', '武汉', '西安', '成都', '大连',
#            '长春', '沈阳', '南京', '济南', '青岛',
#            '杭州', '苏州', '无锡', '宁波', '重庆',
#            '郑州', '长沙', '福州', '厦门', '哈尔滨',
#            '石家庄', '合肥', '惠州', '太原', '昆明',
#            '烟台', '佛山', '南昌', '贵阳', '南宁']
ADDRESS = ['北京']


TYPES = {
	'机械': 'http://b2b.huangye88.com/qiye/jixie/', 
	'五金': 'http://b2b.huangye88.com/qiye/wujin/', 
	'电气': 'http://b2b.huangye88.com/qiye/dianqi/', 
	'机床': 'http://b2b.huangye88.com/qiye/jichuang/', 
	'电子': 'http://b2b.huangye88.com/qiye/dianzi/', 
	'灯饰': 'http://b2b.huangye88.com/qiye/dengshi/', 
	'印刷': 'http://b2b.huangye88.com/qiye/yinshua/', 
	'汽配': 'http://b2b.huangye88.com/qiye/qipei/', 
	'环保': 'http://b2b.huangye88.com/qiye/huanbao/', 
	'工程机械': 'http://b2b.huangye88.com/qiye/gongcheng/', 
	'泵阀': 'http://b2b.huangye88.com/qiye/bengfa/', 
	'纸业': 'http://b2b.huangye88.com/qiye/zhiye/', 
	'安防': 'http://b2b.huangye88.com/qiye/anfang/', 
	'仪器仪表': 'http://b2b.huangye88.com/qiye/yiqiyibiao/', 
	'汽修': 'http://b2b.huangye88.com/qiye/qicheweixiubaoyang/', 
	'通信': 'http://b2b.huangye88.com/qiye/tongxin/', 
	'汽车': 'http://b2b.huangye88.com/qiye/qiche/', 
	'过滤': 'http://b2b.huangye88.com/qiye/guolvfenli/', 
	'消防': 'http://b2b.huangye88.com/qiye/xiaofang/', 
	'汽车用品': 'http://b2b.huangye88.com/qiye/qicheyongpin/', 
	'丝印特印': 'http://b2b.huangye88.com/qiye/siyinteyin/', 
	'加工': 'http://b2b.huangye88.com/qiye/jiagong/', 
	'LED': 'http://b2b.huangye88.com/qiye/led/', 
	'包装': 'http://b2b.huangye88.com/qiye/baozhuang/', 
	'水工业': 'http://b2b.huangye88.com/qiye/shuigongye/', 
	'广电': 'http://b2b.huangye88.com/qiye/guangdian/', 
	'二手设备': 'http://b2b.huangye88.com/qiye/ershoushebei/', 
	'耐火材料': 'http://b2b.huangye88.com/qiye/naihuocailiao/', 
	'焊接切割': 'http://b2b.huangye88.com/qiye/hanjieqiege/', 
	'暖通空调': 'http://b2b.huangye88.com/qiye/nuantongkongtiao/', 
	'添加剂': 'http://b2b.huangye88.com/qiye/tianjiaji/', 
	'纸管': 'http://b2b.huangye88.com/qiye/zhiguan/', 
	'太阳能': 'http://b2b.huangye88.com/qiye/taiyangneng/', 
	'热泵': 'http://b2b.huangye88.com/qiye/rebeng/', 
	'物流设备': 'http://b2b.huangye88.com/qiye/wuliushebei/', 
	'工控': 'http://b2b.huangye88.com/qiye/gongkong/', 
	'IT': 'http://b2b.huangye88.com/qiye/it/', 
	'家电': 'http://b2b.huangye88.com/qiye/jiadian/', 
	'礼品': 'http://b2b.huangye88.com/qiye/lipin/', 
	'家居': 'http://b2b.huangye88.com/qiye/jiaju/', 
	'运动休闲': 'http://b2b.huangye88.com/qiye/yundongxiuxian/', 
	'办公': 'http://b2b.huangye88.com/qiye/bangong/', 
	'家具': 'http://b2b.huangye88.com/qiye/jiajuwang/', 
	'酒店': 'http://b2b.huangye88.com/qiye/jiudian/', 
	'美容美发': 'http://b2b.huangye88.com/qiye/meirong/', 
	'保健品': 'http://b2b.huangye88.com/qiye/baojianpin/', 
	'教育装备': 'http://b2b.huangye88.com/qiye/jiaoyuzhuangbei/', 
	'服装': 'http://b2b.huangye88.com/qiye/fuzhuang/', 
	'服饰': 'http://b2b.huangye88.com/qiye/fushi/', 
	'古玩': 'http://b2b.huangye88.com/qiye/guwan/', 
	'玩具': 'http://b2b.huangye88.com/qiye/wanju/', 
	'制鞋': 'http://b2b.huangye88.com/qiye/zhixie/', 
	'音响灯光': 'http://b2b.huangye88.com/qiye/yinxiangdengguang/', 
	'皮具': 'http://b2b.huangye88.com/qiye/piju/', 
	'小家电': 'http://b2b.huangye88.com/qiye/xiaojiadian/', '零食': 'http://b2b.huangye88.com/qiye/lingshi/', '二手': 'http://b2b.huangye88.com/qiye/ershou/', '珠宝': 'http://b2b.huangye88.com/qiye/zhubao/', '影音': 'http://b2b.huangye88.com/qiye/yingyin/', '智能': 'http://b2b.huangye88.com/qiye/zhineng/', '宠物': 'http://b2b.huangye88.com/qiye/chongwu/', '母婴': 'http://b2b.huangye88.com/qiye/muying/', '商务服务': 'http://b2b.huangye88.com/qiye/fuwu/', '生活服务': 'http://b2b.huangye88.com/qiye/shenghuo/', '广告': 'http://b2b.huangye88.com/qiye/guanggao/', '教育': 'http://b2b.huangye88.com/qiye/jiaoyu/', '交通运输': 'http://b2b.huangye88.com/qiye/jiaotongyunshu/', '物流': 'http://b2b.huangye88.com/qiye/wuliu/', '网站建设': 'http://b2b.huangye88.com/qiye/wangzhan/', '个人贷款': 'http://b2b.huangye88.com/qiye/jinrong/', '项目': 'http://b2b.huangye88.com/qiye/xiangmuhezuo/', '展会': 'http://b2b.huangye88.com/qiye/zhanhui/', '维修': 'http://b2b.huangye88.com/qiye/weixiu/', '创业': 'http://b2b.huangye88.com/qiye/chuangye/', '船舶': 'http://b2b.huangye88.com/qiye/chuanbo/', '翻译': 'http://b2b.huangye88.com/qiye/fanyi/', '建材': 'http://b2b.huangye88.com/qiye/jiancai/', '能源': 'http://b2b.huangye88.com/qiye/nengyuan/', '冶金': 'http://b2b.huangye88.com/qiye/yejin/', '纺织': 'http://b2b.huangye88.com/qiye/fangzhi/', '化工': 'http://b2b.huangye88.com/qiye/huagong/', '表面处理': 'http://b2b.huangye88.com/qiye/biaomianchuli/', '房地产': 'http://b2b.huangye88.com/qiye/fangdichan/', '超硬材料': 'http://b2b.huangye88.com/qiye/chaoyingcailiao/', '塑料': 'http://b2b.huangye88.com/qiye/suliao/', '钢铁': 'http://b2b.huangye88.com/qiye/gangtie/', '橡胶': 'http://b2b.huangye88.com/qiye/xiangjiao/', '皮革': 'http://b2b.huangye88.com/qiye/pige/', '涂料': 'http://b2b.huangye88.com/qiye/tuliao/', '石油': 'http://b2b.huangye88.com/qiye/shiyou/', '石材': 'http://b2b.huangye88.com/qiye/shicai/', '丝网': 'http://b2b.huangye88.com/qiye/siwang/', '卫浴': 'http://b2b.huangye88.com/qiye/weiyu/', '陶瓷': 'http://b2b.huangye88.com/qiye/jianzhutaoci/', '玻璃': 'http://b2b.huangye88.com/qiye/boli/', '养殖': 'http://b2b.huangye88.com/qiye/yangzhi/', '水果批发': 'http://b2b.huangye88.com/qiye/shuiguo/', '食品': 'http://b2b.huangye88.com/qiye/food/', '食品机械': 'http://b2b.huangye88.com/qiye/shipin/', '农机': 'http://b2b.huangye88.com/qiye/nongji/', '园林': 'http://b2b.huangye88.com/qiye/yuanlin/', '农化': 'http://b2b.huangye88.com/qiye/nonghua/', '水产养殖': 'http://b2b.huangye88.com/qiye/shuichanyangzhi/', '茶叶': 'http://b2b.huangye88.com/qiye/chaye/', '饲料': 'http://b2b.huangye88.com/qiye/siliao/', '种子': 'http://b2b.huangye88.com/qiye/zhongzi/', '蔬菜': 'http://b2b.huangye88.com/qiye/shucai/'
	}

MONGO_URI = 'localhost'
MONGO_DB = 'huangye'