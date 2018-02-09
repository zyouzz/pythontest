#!/usr/bin/env python
# -*-coding:utf-8 -*-
__author__ = 'jiang'
from bs4 import BeautifulSoup
import re
with open(r'C:\Users\Esri\Desktop\new11.html') as htt:

    bfcontent = BeautifulSoup(htt, 'lxml')
    i=1
    for qs in bfcontent.find_all('div', 'question'):
        # print i
        qstitles=qs.find_all('div', 'questionContent')[0].text.replace('\n','').replace(u'	','').split(u'、')
        qstitlenum=len(qstitles)
        if qstitlenum>2:
            qstitle = ''.join(qstitles[1:])

        else:
            qstitle=qstitles[1]
        qstitle = re.compile('\((\d)').split(qstitle)[0]
        try:
            if qs.find_all('div', 'questionOptionsRowMode'):
                ss=qs.find_all('div', 'questionOptionsRowMode')[0].find_all('label')

            else:
                ss=qs.find_all('div', 'questionOptions')[0].find_all('label')
            ans = ss[0].text.replace(u' ', '').replace('\n', '')
            bns = ss[1].text.replace(u' ', '').replace('\n', '')
            cns = ss[2].text.replace(u' ', '').replace('\n', '')
            dns = ss[3].text.replace(u' ', '').replace('\n', '')
            sa=qs.find_all('div', 'questionAnswer')[0].text.replace(u'标准答案：', '')
            files = open(r'C:\Users\Esri\Desktop\rs1.txt', 'a+')
            files.write(
                ('%s}%s}%s}%s}%s}%s}%s}%s}%s}%s' % ('1', qstitle, ans+'<br>'+bns+'<br>'+cns+'<br>'+dns, '4', sa, ' ', '4','3','0','0')).encode('utf8') + '\n')
            # print sa
            # if len(sa)>1:
            #     print i,qstitle
        except Exception, e:
            print i
            continue
        # print qstitle
        # print ans,bns,cns,dns
        # print qstitle
        # print qssub
        i+=1

