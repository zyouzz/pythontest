# -*-coding:utf-8 -*-
__author__ = 'jiang'
import arcpy
pdfDoc = arcpy.mapping.PDFDocumentOpen(r'C:\Users\Esri\Desktop\123.pdf')
name11=u'长江流域图'
pdfDoc.updateDocProperties(pdf_title=name11,
                           pdf_author="wangming",
                           pdf_subject="地图集",
                           pdf_keywords="长江",
                           pdf_open_view="USE_THUMBS",
                           pdf_layout="SINGLE_PAGE")
print type('长江流域图')
pdfDoc.saveAndClose()
del pdfDoc