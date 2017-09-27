#!/usr/bin/env python
# -*-coding:utf-8 -*-
# __author__ = 'jiang'
# !/usr/bin/env python
# -*-coding:utf-8 -*-
__author__ = 'jiang'
import collections
import datetime
import os
import re
import urllib.parse
import xlsxwriter
import matplotlib.pyplot as plt
# 注意该模块不支持中文，当出图中有中文时，需要将D:\Python3.6.1\Lib\site-packages\matplotlib\mpl-data\fonts\ttf路径中字体改为支持中文的，如微软雅黑
import pylab as pl
import xlrd
import numpy as np
from numpy import *
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
from email import encoders
from email.header import Header
from email.mime.application import MIMEApplication
from email.mime.image import MIMEImage

'''源数据清洗'''
starttime = datetime.datetime.now()
'''
在windows下面，新文件的默认编码是gbk，这样的话，python解释器会用gbk编码去解析txt，
然而txt此时已经是decode过的unicode编码，这样的话就会导致解析不了，出现上述问题。
解决的办法就是，改变目标文件的编码：file1 = open('C://Users//Esri//Desktop//statistics//原始数据.txt', 'w',encoding='utf-8')
文本文件随手close的习惯：随开随闭
'''
###读取源数据，通过挑选、反编码并写入内存
rootdir = "C://Users//Esri//Desktop//log"
loglist = []
tongjilist = []
for parent, dirnames, filenames in os.walk(rootdir):
    day = 1
    i = 1
    for filename in filenames:
        filedate = filename[7:-4]
        filepath = os.path.join(parent, filename)
        # print(filedate)
        # print(filepath)
        input = open(filepath, 'r')
        num = 1
        for line in input:
            if (
                            'GET //search/ajax/search_result/search_type-questions__q-' and 'template-__page-1' and 'search_type-questions') in line:
                kw1 = line.split()[6][53:-19]
                kw = urllib.parse.unquote(kw1).replace('_', '')
                if '?' in kw:
                    pass
                else:
                    # file1 = open('C://Users//Esri//Desktop//statistics//原始数据.txt', 'a',encoding='utf-8')
                    logline = str(line.split()[0]) + ',' + str(line.split()[3][1:]) + ',' + kw + '\n'
                    loglist.append(logline)
                    # file1 = file1.write(line1)
                    # print(i)
                    i += 1
                    num += 1
        day += 1
        print(filedate + ":共有" + str(num) + "次搜索")
        # file2 = open('C://Users//Esri//Desktop//statistics//每天搜索次数统计.txt', 'a')
        tongjiline = filedate + ',' + str(num) + '\n'
        tongjilist.append(tongjiline)
        # (tongjilist)
        # print(loglist)
        # file2 = file2.write(line2)

###创建文本并写入数据表头
log = open('C://Users//Esri//Desktop//statistics//原始数据.txt', 'w', encoding='utf-8')
loghead = "IP" + ',' + "日期" + ',' + "搜索关键词" + '\n'
log.write(loghead)  # 写文件头
log.close()
tongji = open('C://Users//Esri//Desktop//statistics//每天搜索次数统计.txt', 'w', encoding='utf-8')
tongjihead = "日期" + ',' + "次数" + '\n'
tongji.write(tongjihead)  # 写文件头
tongji.close()

###将内存的list保存到文本中
openlog = open('C://Users//Esri//Desktop//statistics//原始数据.txt', 'a', encoding='utf-8')
openlog.writelines(loglist)
openlog.close()
opentongji = open('C://Users//Esri//Desktop//statistics//每天搜索次数统计.txt', 'a', encoding='utf-8')
opentongji.writelines(tongjilist)
opentongji.close()
del loglist
del tongjilist

day -= 1
sumday = i - 1
print(str(day) + "天一共有：" + str(sumday) + "次搜索")
# print(filedate)
startday = (datetime.datetime.strptime(filedate, "%Y-%m-%d") - datetime.timedelta(days=day - 1)).strftime("%Y-%m-%d")
# print(startday)

'''同一IP、日期、搜索关键词结果去重'''
lines_seen = set()
outfile = open('C://Users//Esri//Desktop//statistics//nodate.txt', "w", encoding='utf-8')
for line in open('C://Users//Esri//Desktop//statistics//原始数据.txt', "r", encoding='utf-8'):
    outfile = open('C://Users//Esri//Desktop//statistics//nodate.txt', "a", encoding='utf-8')
    rline1 = line.split(',')[0]
    # print(rline1)
    rline2 = line.split(',')[2]
    # print(rline2)
    rline3 = line.split(',')[1][:-9]
    # print(rline3)
    reline = rline1 + ',' + rline3 + ',' + rline2
    if reline not in lines_seen:
        # print('reline:'+reline)
        outfile.write(reline)
        lines_seen.add(reline)
opendupbeta = open('C://Users//Esri//Desktop//statistics//nodate.txt', "r", encoding='utf-8')
opendup = open('C://Users//Esri//Desktop//statistics//爬取的数据源.txt', "w", encoding='utf-8')
opendup.write(re.sub(r'IP,,搜索关键词', 'IP,日期,搜索关键词', opendupbeta.read()))
opendupbeta.close()
opendup.close

'''搜索关键词Top100统计'''
outfile1 = open('C://Users//Esri//Desktop//statistics//frequencybeta.txt', "w", encoding='utf-8')
outfile2 = open('C://Users//Esri//Desktop//statistics//爬取的数据源.txt', "r", encoding='utf-8')
for line in outfile2:
    reline1 = line.split(',')[2]
    outfile1.write(reline1)
outfile1.close()
outfile2.close()
f1 = open('C://Users//Esri//Desktop//statistics//frequencybeta.txt', "r", encoding='utf-8')
f2 = open('C://Users//Esri//Desktop//statistics//frequency.txt', 'w', encoding='utf-8')
f2.write(re.sub(r'搜索关键词', '', f1.read()))
f1.close()
f2.close()
openfre = open('C://Users//Esri//Desktop//statistics//frequency.txt', encoding='utf-8')
str1 = openfre.read().lower().split()
# print(str1)
# print("原文本:\n %s"% str1)
# print("\n各词出现的次数：\n %s" % collections.Counter(str1))
# print(type(collections.Counter(str1)))
# cishu= collections.Counter(str1)
# for  ci in str1:
# print(ci, cishu[ci])
# print(collections.Counter(str1)['arcgis'])#以字典的形式存储，每个关键词对应的键值就是在文本中出现的次数
mc100 = re.sub('\ |\[|\]|\(|\)|\'', '', str(collections.Counter(str1).most_common(100)))
# print(mc100)
msarr = mc100.split(',')
# print(type(msarr))
openfre.close()
file3 = open('C://Users//Esri//Desktop//statistics//关键词top100.txt', 'w', encoding='utf-8')
line3 = "关键词" + ',' + "次数" + '\n'
file3_ = file3.write(line3)
i = 1
x = []
y = []
file3.close()
for xunhuan in msarr:
    file4 = open('C://Users//Esri//Desktop//statistics//关键词top100.txt', 'a', encoding='utf-8')
    if i % 2 != 0:
        xunhuandot = xunhuan + ","
        file4.write(xunhuandot)
        x.append(xunhuan)
    else:
        xunhuanbr = xunhuan + '\n'
        file4.write(xunhuanbr)
        y.append(int(xunhuan))
    i += 1
# print(x)
# print(y)
file3.close()
file4.close()

'''搜索关键词Top50统计在线版'''
top50 = open(r'C://Users//Esri//Desktop//statistics//关键词top100.txt', encoding='utf-8').readlines()
print(top50)
da1 = []
fre1 = []
for tx50 in top50:
    da1.append(tx50.split(',')[0])
    fre1.append(tx50.split(',')[1].replace('\n', ''))
file2 = open(r'C:\Hexo\source\html\ArcGIS知乎站内搜索关键词统计Top50.html', encoding='utf-8').readlines()
file2[31] = str(da1[:51]) + ',' + '\n'
file2[33] = str(fre1[:51]) + ',' + '\n'
file1 = open(r'C:\Hexo\source\html\ArcGIS知乎站内搜索关键词统计Top50.html', 'w+', encoding='utf-8')
file1.writelines(file2)
file1.close()

'''top20成图'''
x = x[:20]
y = y[:20]
i = 1
x1 = []
for i in range(1, len(x) + 1):
    x1.append(int(i) + 5)
DataX = tuple(x1)
# print(type(DataX))
DataY = tuple(y)
# print(type(DataY))
fig1 = plt.figure()
fig1.set_size_inches(30, 15)
# plt.xlim()
rects = plt.bar(left=DataX, height=DataY, width=0.5, align="center", yerr=0.000001, facecolor='lightskyblue',
                edgecolor='white')
plt.plot(DataX, DataY)


def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width() / 3., 1.01 * height, '%s' % int(height), color='red', fontsize=25)


autolabel(rects)
plt.xlabel('关键词', fontsize=23)
plt.ylabel('次数', fontsize=23)
plt.title('ArcGIS知乎站内搜索关键词统计（' + startday + '至' + filedate + '）top20统计' + '\n' + '(' + str(day) + "天一共有：" + str(
    sumday) + "次搜索)", fontsize=26)
plt.yticks(fontsize=20)
plt.xticks(DataX, tuple(x), fontsize=20)
savename = "C:/Users/Esri/Desktop/" + re.sub(':', '', str(datetime.datetime.now())) + ".png"
# print(savename)
fig1.savefig(savename, dpi=100)
# plt.show()

'''每天统计成图'''
opentj1 = open('C://Users//Esri//Desktop//statistics//每天搜索次数统计.txt', 'r', encoding='utf-8')
openu1 = open('C://Users//Esri//Desktop//statistics//uheadtongji.txt', 'w', encoding='utf-8')
jishu = 0
for line1 in opentj1.read().split('\n'):
    # print(line1)
    jishu += 1
# print(jishu)
num = 0
opentj2 = open('C://Users//Esri//Desktop//statistics//每天搜索次数统计.txt', 'r', encoding='utf-8')
for line in opentj2.read().split('\n'):
    # print(line)
    openu2 = open('C://Users//Esri//Desktop//statistics//uheadtongji.txt', 'a', encoding='utf-8')
    # print(line3)
    if line == '日期,次数' or line == '':
        pass
    else:
        if num != jishu - 2:
            openu2.write(line + '\n')
        else:
            openu2.write(line)
    num += 1
opentj1.close()
opentj2.close()
f5 = open('C://Users//Esri//Desktop//statistics//uheadtongji.txt', 'r').read().replace('\n', ',').split(',')
# print(f5)
jishu2 = 1
x = []
y = []
for uh in f5:
    # print(uh)
    if jishu2 % 2 != 0:
        x.append(uh)
    else:
        y.append(int(uh))
    jishu2 += 1
# (x)
# print(y)

jishu1 = 1
x1 = []
for jishu1 in range(1, len(x) + 1):
    x1.append(int(jishu1))
# print(x1)
DataX = tuple(x1)
# print(type(DataX))
DataY = tuple(y)
# print(type(DataY))
# fig2 = plt.figure()
# fig2.set_size_inches(30, 10.5)
# rects = plt.scatter(x1, y, c='r', s=100, marker='o')
# plt.xlabel('日期(' + startday + '+)', fontsize=20)
# plt.ylabel('次数', fontsize=20)
# plt.title(
#     'ArcGIS知乎站内搜索每天统计（' + startday + '至' + filedate + '）' + '\n' + '(' + str(day) + "天一共有：" + str(sumday) + "次搜索)",
#     fontsize=26)
# plt.xticks(fontsize=16)
# plt.yticks(fontsize=16)
# # plt.xticks(DataX,tuple(x),fontsize=16)
# saveday = "C:/Users/Esri/Desktop/" + re.sub(':', '', str(datetime.datetime.now())) + ".png"
# # print(savename)
# fig2.savefig(saveday, dpi=100)
# plt.show()

'''每天统计成图在线版'''
dayst = open(r'C://Users//Esri//Desktop//statistics//每天搜索次数统计.txt', encoding='utf-8').readlines()
print(dayst)
da = []
fre = []
for tx1 in dayst:
    da.append(tx1.split(',')[0])
    fre.append(tx1.split(',')[1].replace('\n', ''))
file = open(r'C:\Hexo\source\html\ArcGIS知乎每天站内搜索统计.html', encoding='utf-8').readlines()
file[31] = str(da) + ',' + '\n'
file[33] = str(fre) + ',' + '\n'
file1 = open(r'C:\Hexo\source\html\ArcGIS知乎每天站内搜索统计.html', 'w+', encoding='utf-8')
file1.writelines(file)
file1.close()
'''自动git push'''

'''按月份统计汇总'''
openutj = open('C://Users//Esri//Desktop//statistics//uheadtongji.txt', "r", encoding='utf-8')
umonth = []
for line5 in openutj.read().split('\n'):
    umonth.append(line5[:7])
# print(year)
# print(month)
openutj.close()
outfile7 = open('C://Users//Esri//Desktop//statistics//每月搜索次数统计.txt', "w", encoding='utf-8')
headms = '月份' + ',' + '次数' + '\n'
outfile7.write(headms)
outfile7.close()
uyemon = []
for mon in umonth:
    # print(mon)
    openutj1 = open('C://Users//Esri//Desktop//statistics//uheadtongji.txt', "r", encoding='utf-8')
    summ = 0
    for line6 in openutj1.read().split('\n'):
        monn = line6[:7]
        if monn == mon:
            summ += int(line6[11:])
    uyemon.append(summ)
# print(uyemon)
month = []
for dmonth in umonth:
    if dmonth not in month:
        month.append(dmonth)
# print(month)
yemon = []
for dyemon in uyemon:
    if dyemon not in yemon:
        yemon.append(dyemon)
# print(yemon)
openutj1.close()
i22 = 0
sousuo = []
for c22 in month:
    i22 += 1
    if i22 != len(month):
        sousuo.append(str(c22) + ',' + str(yemon[i22 - 1]) + '\n')
    else:
        sousuo.append(str(c22) + ',' + str(yemon[i22 - 1]))
# print(sousuo)
openmeiyue = open('C://Users//Esri//Desktop//statistics//每月搜索次数统计.txt', "a", encoding='utf-8')
openmeiyue.writelines(sousuo)
# print(sousuo)
openmeiyue.close()

'''每天统计折点图'''
fig3 = pl.figure()
fig3.set_size_inches(30, 10.5)
plt.title(
    'ArcGIS知乎站内搜索每天统计（' + startday + '至' + filedate + '）' + '\n' + '(' + str(day) + "天一共有：" + str(sumday) + "次搜索)",
    fontsize=26)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.xlabel('日期(' + startday + '+)', fontsize=23)
plt.ylabel('次数', fontsize=23)
plt.plot(x1, y, 'b*')  # use pylab to plot x and y
plt.plot(x1, y, 'r')
for i, (_x, _y, _z) in enumerate(zip(x1, y, y)):
    plt.text(_x, _y, _z, color='red', fontsize=25)
savets = "C:/Users/Esri/Desktop/" + re.sub(':', '', str(datetime.datetime.now())) + "ts.png"
fig3.savefig(savets, dpi=100)
# pl.show()  # show the plot on the screen

'''每月统计折点图'''
openmonth = open('C://Users//Esri//Desktop//statistics//每月搜索次数统计.txt', 'r', encoding='utf-8')
realmonth = []
monsta = []
for monybeta in openmonth:
    mony = monybeta.replace('\n', '').split(',')[1]
    if mony != '次数':
        monsta.append(mony)
        realmonth.append(monybeta[5:7])
mons = []
# print(len(monsta))
for monx in range(0, len(monsta)):
    mons.append(monx + 1)
# print(monsta)
# print(mons)
fig4 = plt.figure()
fig4.set_size_inches(30, 10.5)
plt.title(
    'ArcGIS知乎站内搜索每月统计（' + startday + '至' + filedate + '）' + '\n' + '(' + str(day) + "天一共有：" + str(sumday) + "次搜索)",
    fontsize=26)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.xlabel('月份(' + str(startday)[5:7] + '月份开始--)', fontsize=23)
plt.ylabel('次数', fontsize=23)
plt.plot(mons, monsta, 'bo', mons, monsta, 'r')  # use pylab to plot x and y
# plt.plot(mons, monsta, 'r')
plt.xticks(mons, realmonth, fontsize=20)
for i, (_x, _y, _z) in enumerate(zip(mons, monsta, monsta)):
    plt.text(_x, _y, _z, color='red', fontsize=25)
savemonth = "C:/Users/Esri/Desktop/" + re.sub(':', '', str(datetime.datetime.now())) + "month.png"
fig4.savefig(savemonth, dpi=100)

'''txt转xlsx'''


def txt_to_xlsx(txtpath):
    exc = xlsxwriter.Workbook(
        'C://Users//Esri//Desktop//statistics//' + txtpath.split('//')[-1].split('.')[0] + '.xlsx')
    worksheet = exc.add_worksheet()
    openf = open(txtpath, 'r', encoding='utf-8')
    opentxt = openf.read().split('\n')
    txtline = 0
    spaceline = 0
    storesp = set()
    newtxt = []
    '''首先去掉空行'''
    for line in opentxt:
        # print(line)
        txtline += 1
        if line != '':
            newtxt.append(line)
        else:
            spaceline += 1
            storesp.add(txtline)

    '''将内存中list写入xlsx'''
    colnums = len(newtxt[0].split(','))
    maxwidth = 0
    linenum = len(newtxt)
    for colnum in range(0, colnums):
        for linenums in range(0, linenum):
            wid = len(newtxt[linenums].split(',')[colnum])
            if wid >= maxwidth:
                maxwidth = wid
        worksheet.set_column(colnum, colnum, width=maxwidth)
        for linenumss in range(0, linenum):
            worksheet.write(linenumss, colnum, newtxt[linenumss].split(',')[colnum])
    exc.close()
    openf.close()
    # '''文本信息'''
    # print('====================================='+'\n'+'导入文本信息'+'\n'+'=====================================')
    # print('该文本共有%d行' % txtline + '\n' + '有%d行为空' % spaceline + '\n' + '空行行数分别为:' + re.sub('{|}', '', str(storesp)))


txt_to_xlsx('C://Users//Esri//Desktop//statistics//爬取的数据源.txt')
txt_to_xlsx('C://Users//Esri//Desktop//statistics//每天搜索次数统计.txt')
txt_to_xlsx('C://Users//Esri//Desktop//statistics//每月搜索次数统计.txt')
txt_to_xlsx('C://Users//Esri//Desktop//statistics//关键词top100.txt')

'''Top100成图'''
top100 = xlrd.open_workbook(r'C:\Users\Esri\Desktop\statistics\关键词top100.xlsx')
try:
    topsheet = top100.sheet_by_name('Sheet1')
except:
    print('no sheet in xlsx named Sheet1')
nrows = topsheet.nrows
ncols = topsheet.ncols
col1 = []
col2 = []
filters = ['for', 'not', 'to', 'be', 'the', 'is', 'in', 'a', 'create', 'no']
num = 1
for i in range(1, nrows):
    row_data = topsheet.row_values(i)
    if row_data[0] not in filters:
        col1.append(row_data[0])
        col2.append(int(row_data[1]))
        num += 1
print(num)
print(col1)
print(col2)
##为了方便展示，翻转一下关键词和次数，
keyw = tuple(reversed(col1))
col3 = []
##翻转函数reversed()结果是一个迭代，需要重新创建list
for sornew in reversed(col2):
    col3.append(sornew)
data = np.array(col3)
x = np.arange(len(col1))
fig = plt.figure()
fig.set_size_inches(20, 30)
ax1 = plt.axes([0.07, 0.03, 0.9, 0.93])
area = ax1.barh(x, data, align='center', color='g', alpha=0.5)
plt.ylim(-1, num)
plt.xlabel('data', size=18, color='k')
ax1.set_yticks(x)
ax1.set_yticklabels(keyw)
plt.xlabel('次数', fontsize=23)
plt.ylabel('关键词', fontsize=23)
plt.title('ArcGIS知乎站内搜索关键词统计', fontsize=30)


###加标注
def autolabel(area):
    numm = 1
    for rect1 in area:
        height = rect1.get_width()
        print(int(height))
        # plt.text(rect1.get_x() + rect1.get_width() / 3., 1.01 * height, '%s' % int(height), color='red', fontsize=25)
        plt.text(height + 1, numm - 1, '%s' % int(height), color='red')
        numm += 1


autolabel(area)

fig.savefig(r'C:\Users\Esri\Desktop\top100.png', dpi=100)

'''发送邮件'''
# _user = "jiangbh@esrichina.com.cn"
# smtpserver='smtp.esrichina.com.cn'
# _from = '江宝骅<jiangbh@esrichina.com.cn>'
# _pwd = "*********"
# #----如果发送多个人用英文半角逗号隔开---
# _to = '江宝骅<jiangbh@esrichina.com.cn>'
#
# '''我们编写了一个函数_format_addr()来格式化一个邮件地址。
# 注意不能简单地传入name <addr@example.com>，
# 因为如果包含中文，需要通过Header对象进行编码。----廖雪峰'''
# def _format_addr(s):
#     name, addr = parseaddr(s)
#     return formataddr((Header(name, 'utf-8').encode(), addr))
#
# # 如名字所示Multipart就是分多个部分
# msg = MIMEMultipart()
# msg["Subject"] = "ArcGISzhihu站内搜索词统计"
# msg["From"] =_format_addr( _from)
# msg["To"] = _to
#
# # ---这是文字图片部分---
# def addimg(src, imgid):# 添加图片函数，参数1：图片路径，参数2：图片id
#     fp = open(src, 'rb')# 打开文件
#     msgImage = MIMEImage(fp.read())# 创建MIMEImage对象，读取图片内容并作为参数
#     fp.close()# 关闭文件
#     msgImage.add_header('Content-ID', imgid)# 指定图片文件的Content-ID，imgid，<img>标签中的src用到
#     return msgImage# 返回msgImage对象
# #msg = MIMEMultipart('related')# 创建MIMEMultipart对象，采用related定义内嵌资源的邮件体
# #msg["Subject"] = "ArcGISzhihu"
# part = MIMEText('<font size="18px" color=red><b><center>ArcGIS知乎站内搜索关键词统计（详情见附件）</center></b></font>'+'<br/><b><center>数据图表获取生成时间：'+str(datetime.datetime.now())+'</center></b><img width="1300px" src="cid:pic">',"html","utf-8" )
# msg.attach(part)
# # image = MIMEImage(open('C://Users//Esri//Desktop//0b7b02087bf40ad14cc91cbd5f2c11dfa9eccebb.jpg','rb').read()).add_header('Content-ID','men')
# msg.attach(addimg(savename,"pic"))
#
# # ---这是附件部分---
#
# part = MIMEApplication(open('C://Users//Esri//Desktop//statistics//爬取的数据源.xlsx', 'rb').read())
# part.add_header('Content-Disposition', 'attachment', filename=('gbk', '',"爬取的数据源.xlsx"))
# msg.attach(part)
#
# part = MIMEApplication(open('C://Users//Esri//Desktop//statistics//每天搜索次数统计.txt', 'rb').read())
# part.add_header('Content-Disposition', 'attachment', filename=('gbk', '',"每天搜索次数统计.xlsx"))
# msg.attach(part)
#
# part = MIMEApplication(open('C://Users//Esri//Desktop//statistics//每月搜索次数统计.xlsx', 'rb').read())
# part.add_header('Content-Disposition', 'attachment', filename=('gbk', '',"每月搜索次数统计.xlsx"))
# msg.attach(part)
#
# part = MIMEApplication(open('C://Users//Esri//Desktop//statistics//关键词top100.xlsx', 'rb').read())
# part.add_header('Content-Disposition', 'attachment', filename=('gbk', '',"关键词top100.xlsx"))
# msg.attach(part)
#
# part = MIMEApplication(open(savename, 'rb').read())
# part.add_header('Content-Disposition', 'attachment', filename=('gbk', '',"Top20统计结果直方图.png"))
# msg.attach(part)
#
# part = MIMEApplication(open(savets, 'rb').read())
# part.add_header('Content-Disposition', 'attachment', filename=('gbk', '',"每天统计结果折点图.png"))
# msg.attach(part)
#
# part = MIMEApplication(open(savemonth, 'rb').read())
# part.add_header('Content-Disposition', 'attachment', filename=('gbk', '',"每月统计结果折点图.png"))
# msg.attach(part)
#
# s = smtplib.SMTP(smtpserver,25)  # 连接smtp邮件服务器,端口默认是25
# s.login(_user, _pwd)  # 登陆服务器
# s.sendmail(_user, _to.split(','), msg.as_string())  # 发送邮件
# s.close()

'''执行操作时间'''
endtime = datetime.datetime.now()
time = (endtime - starttime).seconds
print('------------------------------------------------------' + '\n' + "一共用时" + str(time) + "秒")
# print('邮件发送给:%s'%_to.split(','))
