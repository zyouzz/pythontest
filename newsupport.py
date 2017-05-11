#!/usr/bin/env python
# -*-coding:utf-8 -*-
__author__ = 'jiang'
import  requests
post_data={"productRequest":{"ProductLevel1":"Desktop","ProductLevel2":"arcgis-desktop","ProductLevel3":"arcmap","ProductLevel4":"10-5"},"searchRequest":{"SearchText":'null',"PageNo":'2',"NoOfResultsPerPage":'10',"KbType":"Technical Articles","KbContentType":'null',"IssueCtg":'null',"IssueSubCtg":'null',"ReloadPagination":'true',"TimeFilter":'null'}}
return_data=requests.post("http://support.esri.com/ProductDetails/GetKBResults",data=post_data)
print return_data.text