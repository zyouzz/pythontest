#!/usr/bin/env python
# -*-coding:utf-8 -*-
__author__ = 'jiang'
import eyed3
import wave
import os
import speech_recognition as sr
from pydub import AudioSegment
import time
import datetime
#获取音频时长
import wave
# ffff='D:/mapping2.wav'
# fii = wave.open(ffff,'r')
# timelength=int(fii.getparams()[3]/fii.getparams()[2])
# print(int(5.6))
#
# ##音频分割输出
# readaudio=AudioSegment.from_wav(ffff)
# kn=int(timelength/8)+1
# for i in range(8):
#      readaudio[i*kn*1000:((i+1)*kn+2)*1000].export(r'C:\Users\Esri\Desktop\speech\m2d%d.wav'%(i+1), format="wav")
# 获取文件夹下的音频文件名
starttime = datetime.datetime.now()
i = 1
for name in os.listdir(r'C:\Users\Esri\Desktop\speech'):
    print("%d %s 开始转换" % (i, name))
    ##音频分块识别
    r = sr.Recognizer()
    # for i in range(kn):
    try:
        with sr.WavFile(r'C:\Users\Esri\Desktop\speech\%s' % name) as source:
            audio = r.record(source)
            IBM_USERNAME = '96f63d9d-1053-4675-9acd-e57763d7995a'
            IBM_PASSWORD = 'Tb8IWEcfcQUu'
            text = r.recognize_ibm(audio, username=IBM_USERNAME, password=IBM_PASSWORD, language='en-US')
            print(text)
            open(r'C:\Users\Esri\Desktop\text\%s.txt' % name, 'a+').write(text)
            temptime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print('%s %d %s 已完成' % (temptime,i, name))
            time.sleep(30)
            i+=1

    except Exception as e:
        i += 1
        print(e)
        temptime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print('%s %d %s 未完成' % (temptime, i, name))
        continue
jietime = datetime.datetime.now()
last=jietime-starttime
print('总共花费时间：%s'%last)
