#!/usr/bin/env python
# -*-coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
import sys
import  re
reload(sys)
sys.setdefaultencoding('utf-8')
pageinfo=[]
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'}
__author__ = 'jiang'
# city_citys=['http://flight.qunar.com/schedule/fsearch_list.jsp?departure=珠海&arrival=北京','http://flight.qunar.com/schedule/fsearch_list.jsp?departure=珠海&arrival=长春','http://flight.qunar.com/schedule/fsearch_list.jsp?departure=珠海&arrival=长沙','http://flight.qunar.com/schedule/fsearch_list.jsp?departure=珠海&arrival=常州','http://flight.qunar.com/schedule/fsearch_list.jsp?departure=珠海&arrival=成都','http://flight.qunar.com/schedule/fsearch_list.jsp?departure=珠海&arrival=重庆']



# ss = open(r'C:\Users\Esri\Desktop\vvv\%s.txt'%ft, 'w')
# ss.write(cccc.encode('utf-8'))
# time.sleep(15)
# print BeautifulSoup(hbpage, 'lxml').select('div[class="result_content"]')[0].get_text()
def flyin():
    pageinfo = []
    files = open(r'C:\Users\Esri\Desktop\url.txt', 'r')
    urls = []
    for url in files.read().split():
        urls.append(url)
    for city_city in urls:
        print city_city
        hbpage = requests.get(city_city, headers=headers).text
        # print hbpage
        bg = str(city_city.split('=')[-2]).replace('&arrival', '')  # 始发
        dg = city_city.split('=')[-1]  # 飞往
        ft = (bg + dg)
        print ft
        if BeautifulSoup(hbpage, 'lxml').select('p[class="msg2"]'):
            print '此线路无航班'
        else:
            try:
                #航班里程
                # print BeautifulSoup(hbpage, 'lxml').select('p[class="msg2"]')[0].get_text()

                hblc = BeautifulSoup(hbpage, 'lxml').select('em')[0].get_text()
                print hblc
                #航班班次 第一列
                hbtitle=BeautifulSoup(hbpage,'lxml').select('span[class="title"]')
                hbbc1=[]
                hkgs1=[]
                jixing1=[]
                for ht in hbtitle:
                    hbbc=re.findall(r'\w.?\d*',ht.get_text())[0]#航班班次
                    hkgs=ht.get_text().split(hbbc)[0]#航空公司
                    jixing=ht.get_text().split(hbbc)[1]#机型
                    hbbc1.append(hbbc)
                    hkgs1.append(hkgs)
                    jixing1.append(jixing)
                #起降时间 第二列
                hbtime=BeautifulSoup(hbpage,'lxml').select('span[class="c2"]')[1:]
                qfsj1=[]
                jlsj1=[]
                for qj in hbtime:
                    qfsj=qj.get_text()[:5]#起飞时间
                    jlsj=qj.get_text()[5:]#降落时间
                    qfsj1.append(qfsj)
                    jlsj1.append(jlsj)

                #机场 第三列
                hbjc=BeautifulSoup(hbpage,'lxml').select('span[class="c3"]')[1:]
                qfjc1=[]
                jljc1=[]
                for jc in hbjc:
                    qfjc=jc.get_text().split('机场'.decode('utf-8'))[0]+'机场'.decode('utf-8')#起飞机场
                    jljc=jc.get_text().split('机场'.decode('utf-8'))[1]+'机场'.decode('utf-8')#降落机场
                    qfjc1.append(qfjc)
                    jljc1.append(jljc)

                #准点率 第四列
                zdl=BeautifulSoup(hbpage,'lxml').select('span[class="c4"]')[1:]
                zdl1=[]
                wdsj1=[]
                for zd in zdl:
                    zdlv=zd.get_text().split('%')[0]+'%'
                    wdsj=zd.get_text().split('%')[1]
                    zdl1.append(zdlv)
                    wdsj1.append(wdsj)


                #班期 第五列
                bq=BeautifulSoup(hbpage,'lxml').select('span[class="c5"]')[1:]
                # xx=[]
                duty1 = []
                for xq in bq:
                    week=re.split('\">\d</span>',str(xq))[:-1]
                    print week
                    week1=[]
                    ii=1
                    for day in week:
                        # print day
                        if ii==1:
                            dd='周一'
                        elif ii==2:
                            dd = '周二'
                        elif ii==3:
                            dd = '周三'
                        elif ii==4:
                            dd = '周四'
                        elif ii==5:
                            dd = '周五'
                        elif ii==6:
                            dd = '周六'
                        elif ii==7:
                            dd = '周日'
                        if day[-4:]=='blue':
                            duty='%s有班期'%dd
                        else:
                            duty='%s没有班期'%dd
                        ii+=1
                        week1.append(duty)
                    duty1.append(week1)

                #经停 第六列
                # driver=webdriver.PhantomJS(executable_path=r"D:\Python27\phantomjs-2.1.1-windows\bin\phantomjs")
                # link='http://flight.qunar.com/schedule/fsearch_list.jsp?departure=北京&arrival=海口'
                # driver.get(link)
                # # time.sleep(5)
                # jt = BeautifulSoup(hbpage, 'lxml').select('span[class="c6"]')[1:]
                # print jt
                # for jt1 in jt:
                #     jthb = jt1.get_text()
                #     print jthb

                #班期有效期 第七列
                bqyxq = BeautifulSoup(hbpage, 'lxml').select('span[class="c7"]')[1:]
                qs1=[]
                js1=[]
                for yxq in bqyxq:

                    yxs=yxq.get_text()[:10]#起始
                    yxe=yxq.get_text()[:10]#结束
                    qs1.append(yxs)
                    js1.append(yxe)

                print hbbc1
                print duty1
                for li in range(len(hbbc1)):
                    print li
                    print '标记'
                    pageinfo.append(bg + ',' + dg + ',' + hblc + ',' + hbbc1[li] + ',' + hkgs1[li] + ',' + jixing1[li] + ',' + qfsj1[li] + ',' + jlsj1[li] + ',' + qfjc1[li] + ',' + jljc1[li] + ',' + zdl1[li] + ',' + wdsj1[li] + ',' + duty1[li][0] + ',' + duty1[li][1] + ',' + duty1[li][2] + ',' +duty1[li][3] + ',' + duty1[li][4] + ',' + duty1[li][5] + ',' + duty1[li][6] + ',' + qs1[li] + ',' + js1[li] + '\n')
                    print bg + ',' + dg + ',' + hblc + ',' + hbbc1[li] + ',' + hkgs1[li] + ',' + jixing1[li] + ',' + qfsj1[li] + ',' + jlsj1[li] + ',' + qfjc1[li] + ',' + jljc1[li] + ',' + zdl1[li] + ',' + wdsj1[li] + ',' + duty1[li][0] + ',' + duty1[li][1] + ',' + duty1[li][2] + ',' +duty1[li][3] + ',' + duty1[li][4] + ',' + duty1[li][5] + ',' + duty1[li][6] + ',' + qs1[li] + ',' + js1[li] + '\n'
                    acc=bg + ',' + dg + ',' + hblc + ',' + hbbc1[li] + ',' + hkgs1[li] + ',' + jixing1[li] + ',' + qfsj1[li] + ',' + jlsj1[li] + ',' + qfjc1[li] + ',' + jljc1[li] + ',' + zdl1[li] + ',' + wdsj1[li] + ',' + duty1[li][0] + ',' + duty1[li][1] + ',' + duty1[li][2] + ',' +duty1[li][3] + ',' + duty1[li][4] + ',' + duty1[li][5] + ',' + duty1[li][6] + ',' + qs1[li] + ',' + js1[li] + '\n'
                    filers = open(r'C:\Users\Esri\Desktop\url56.txt', 'a+')
                    filers.write(str(acc).encode('utf-8'))
            except Exception, e:
                print e
                print ft + '网页出错'
                continue
    return pageinfo
if __name__=='__main__':
    # print flyin()
    aa=flyin()
    print aa
