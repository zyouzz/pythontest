#!/usr/bin/env python
#-*-coding:utf-8 -*-
__author__ = 'jiang'
# 导入模块 urllib2
import urllib2
import BeautifulSoup
import re
import datetime
starttime = datetime.datetime.now()
#file = open('C://Users//Esri//Desktop//arcgiazhihu.txt', 'a')
#line ="编号"+ ',' + "用户名"+ ',' + "威望" + ',' + "积分" + ',' + "赞同" + ',' + "感谢" + ',' + "发问" + ',' + "回复" + ',' + "文章" + ',' + "关注" + ',' + "被关注" + ',' + "关注话题" + ',' +"个人主页" + ',' +"个性主页" + '\n'
# 对象file的write方法将字符串line写入file中.
#file = file.write(line)
num=0
start=input("请输入需要爬取开始：")
shuliang=input("请输入需要爬取的用户数量：")
for namecode in range(start,shuliang+1):
    url = 'http://zhihu.esrichina.com.cn/people/' + str(namecode)
    #print(url)
    # 设置头文件。抓取有些的网页不需要专门设置头文件，但是这里如果不设置的话，
    # google会认为是机器人不允许访问。另外访问有些网站还有设置Cookie，这个会相对复杂一些，
    # 这里暂时不提。关于怎么知道头文件该怎么写，一些插件可以看到你用的浏览器和网站交互的
    # 头文件（这种工具很多浏览器是自带的），我用的是firefox的firebug插件。
    header = {'Host': 'zhihu.esrichina.com.cn','User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:26.0) Gecko/20100101 Firefox/26.0','Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8','Connection': 'keep-alive'}
    # 建立连接请求，这时google的服务器返回页面信息给con这个变量，con是一个对象
    try:
        req = urllib2.Request(url, headers = header)
        con = urllib2.urlopen( req )
        # 对con这个对象调用read()方法，返回的是html页面，也就是有html标签的纯文本
        doc = con.read()
        #print doc
        # 生成一个soup对象，doc就是步骤二中提到的
        soup = BeautifulSoup.BeautifulSoup(doc)
        # 抓取论文标题，作者，简短描述，引用次数，版本数，引用它的文章列表的超链接
        # 这里还用了一些正则表达式，不熟悉的先无知它好了。至于'class' : 'gs_rt'中.鐣欏璁哄潧-涓€浜�-涓夊垎鍦�
        # 'gs_rt'是怎么来的，这个是分析html文件肉眼看出来的。上面提到的firebug插件
        # 让这个变的很简单，只要一点网页，就可以知道对应的html 标签的位置和属性，
        # 相当好用。
        user_name = soup.html.body.find('div', {'class': 'mod-head'}).h1
        #print user_name
        str123=str(user_name)
        user_name1 = re.sub(r'\s|<h1>|<.*>', '', str123)
        weiwang1 = soup.findAll('em', {'class': 'aw-text-color-green'})
        chengjiu1=soup.findAll('em', {'class': 'aw-text-color-orange'})
        q_a = soup.findAll('span', {'class': 'badge'})
        fensi = soup.findAll('em', {'class': 'aw-text-color-blue'})
        weiwang2=weiwang1[0:len(weiwang1) / 2]
        chengjiu=chengjiu1[0:len(chengjiu1) / 2]
        weiwang = re.sub(r'<em class="aw-text-color-green">|<.*>', '', str(weiwang2[0]))
        jifen=re.sub(r'<em class="aw-text-color-orange">|<.*>', '', str(chengjiu[0]))
        zantong = re.sub(r'<em class="aw-text-color-orange">|<.*>', '', str(chengjiu[1]))
        ganxie = re.sub(r'<em class="aw-text-color-orange">|<.*>', '', str(chengjiu[2]))
        fawen=re.sub(r'<span class="badge">|<.*>', '', str(q_a[0]))
        huifu=re.sub(r'<span class="badge">|<.*>', '', str(q_a[1]))
        wenzhang=re.sub(r'<span class="badge">|<.*>', '', str(q_a[2]))
        guanzhu=re.sub(r'<em class="aw-text-color-blue">|<.*>', '', str(fensi[0]))
        beiguanzhu = re.sub(r'<em class="aw-text-color-blue">|<.*>', '', str(fensi[1]))
        guanzhuhuati = re.sub(r'\n|<em class="aw-text-color-blue">|<.*>', '', str(fensi[2]))
        gerenzhuye='http://zhihu.esrichina.com.cn/people/'+str(namecode)
        gexingzhuye='http://zhihu.esrichina.com.cn/people/'+user_name1
        print "正在爬取用户【"+str(namecode)+str(user_name1)+"】的信息"
        # print "威望：" + weiwang
        # print "积分：" + jifen
        # print "赞同：" + zantong
        # print "感谢：" + ganxie
        # print "提问：" + fawen
        # print "回复：" + huifu
        # print "文章：" + wenzhang
        # print "个人主页："+gerenzhuye
        # print "个性主页："+gexingzhuye
        # print "--------------------------------------------------------------------------------------------------------------------------------------"
        file = open('C://Users//Esri//Desktop//arcgiazhihu.txt', 'a')
        line = str(namecode)+ ',' +str(user_name1)+ ',' + weiwang + ',' + jifen + ',' + zantong+ ',' + ganxie+ ',' + fawen+ ',' + huifu+ ',' + wenzhang+ ',' + guanzhu+ ',' + beiguanzhu+ ',' + guanzhuhuati +',' +gerenzhuye+',' +gexingzhuye+ '\n'
        # 对象file的write方法将字符串line写入file中
        file = file.write(line)
        num=num+1
    except Exception, e:
        print "用户"+str(namecode)+"不存在"
        continue
endtime = datetime.datetime.now()
time = (endtime - starttime).seconds
print "最终共爬取到"+str(num)+"个有效用户信息"
print "用时"+str(time)+"秒"



