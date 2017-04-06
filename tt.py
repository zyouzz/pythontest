import arcpy
import urllib
import json
import os
url1="http://192.168.100.157:6080/arcgis/rest/services/MyMapService/MapServer?f=pjson"
urlread=urllib.urlopen(url1).read()
f=open("D:\\json.txt","w")
f.write(urlread)
f.close()
