最近帮朋友做一些网络营销的工作，需要抓取一些客源信息，用以辅助营销，我感觉很多做电商的朋友，尤其是微商朋友们，应该都是比较需要各种客源信息的吧，今天，小编我就借此机会把利用python多进程的方式抓取黄页海量的客源信息的方法分享给大家，希望大家能多多关注本人，多讨论关于爬虫和数据挖掘分析相关的问题。

该代码已经上传至本人的github，喜欢的朋友可到我的公众号获取。

一、特别提到的库：

多进程：pool

mogo数据库：pymongo

自然语言编码转换：codecs

二、特别推荐—-jupyter

做开发没有趁手的兵器是不行的，对于python脚本的开发以及做一些数据挖掘和分析这方面工作来说，jupyter notebook这个工具是一个非常合适的工具，它可以保存你写的阶段性的小脚本，同时，又不至于像ipython那样把有价值的历史代码被滚屏所淹没，关于这个工具的其他优点，大家可以自行百度，总之，这是一个python开发的一个神器，借助它可以快速的写出很多高效的代码出来。
![Alt text](http://timg01.bdimg.com/timg?pacompress&imgtype=0&sec=1439619614&autorotate=1&di=e919419efee87d9f43eba30c79a90517&quality=60&size=b640_10000&src=http%3A%2F%2Fbos.nj.bpc.baidu.com%2Fv1%2Fmediaspot%2Fa88381b4d3bfdf3981af77a1001440b4.png)

​三、主要代码：

这次抓取的站点是黄页88网，网站放置行业信息的结构是这样的，按照行业来抓取的话，首先是分为各种行业，每种行业下面又可以获取到各个省份的该行业的信息。
![Alt text](http://timg01.bdimg.com/timg?pacompress&imgtype=0&sec=1439619614&autorotate=1&di=d96ab7329f804b24c30f8e39eb13b7e8&quality=60&size=b640_10000&src=http%3A%2F%2Fbos.nj.bpc.baidu.com%2Fv1%2Fmediaspot%2F0484ff7a976660ce2769ea879938e588.png)
![Alt text](http://timg01.bdimg.com/timg?pacompress&imgtype=0&sec=1439619614&autorotate=1&di=cfdc3d4a8c54950da097883fadca80b7&quality=60&size=b640_10000&src=http%3A%2F%2Fbos.nj.bpc.baidu.com%2Fv1%2Fmediaspot%2Fd7373cd464c7ffa9670a59c25f931acc.png)

为了能够按照行业进行抓取，我们可以先把首页出现的行业分类抓取下来，保存为字典，这一步的方法就不仔细说了，请自行解决。我已经保存好了字典，将起保存在一个单独的配置文件中，方便调用时使用。
![Alt text](http://timg01.bdimg.com/timg?pacompress&imgtype=0&sec=1439619614&autorotate=1&di=36039676c3e63c969a0a944e86450c2a&quality=60&size=b640_10000&src=http%3A%2F%2Fbos.nj.bpc.baidu.com%2Fv1%2Fmediaspot%2F047e4e00fbe5b818e4222e1294c46938.png)
获取各个行业对应的每个省的url，我们可以写一个函数来完成，返回一个url的列表。
![Alt text](http://timg01.bdimg.com/timg?pacompress&imgtype=0&sec=1439619614&autorotate=1&di=42459f68da09d48bf9c5586287bba8fb&quality=60&size=b640_10000&src=http%3A%2F%2Fbos.nj.bpc.baidu.com%2Fv1%2Fmediaspot%2F783316289cbf445affced00386975d26.png)
有了这个url以后，就可以直接得到内容了，其中翻页的时候需要注意url中控制页码是通过pn变量实现的，也需要对最后一页做一下判断，否则就会形成死循环。这一步就已经把数据写入了txt文件中。
![Alt text](http://timg01.bdimg.com/timg?pacompress&imgtype=0&sec=1439619614&autorotate=1&di=1cfb3fb2350c529de8ef5daa13d9b9e0&quality=60&size=b640_10000&src=http%3A%2F%2Fbos.nj.bpc.baidu.com%2Fv1%2Fmediaspot%2F362e03d3684604fda7a6d3c4631eebd9.png)

最后是执行爬虫的的代码，这里用到了多线程，同时需要存入mongodb的数据库。
![Alt text](http://timg01.bdimg.com/timg?pacompress&imgtype=0&sec=1439619614&autorotate=1&di=6eeffc9fa4cc3c380bbfd14be89809e3&quality=60&size=b640_10000&src=http%3A%2F%2Fbos.nj.bpc.baidu.com%2Fv1%2Fmediaspot%2Ffd1043b25bc8c427006aa50ded059c5e.png)

由于自媒体发布的时候贴代码不太方便，感兴趣的朋友关注我的同名订阅号获取github地址吧！
