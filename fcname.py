import arcpy
arcpy.env.workspace="D:\\test\layer1008.gdb"
layers=arcpy.ListFeatureClasses()
for layer in layers:
    layerName=layer[:]
    arcpy.AddField_management(layer,"layername","TEXT")
    arcpy.CalculateField_management(layer,"layername","'"+layerName+"'","PYTHON")
