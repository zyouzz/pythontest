import arcpy
import time

# Script Tool Parameters
InputFeature = arcpy.GetParameterAsText(0)
Order = arcpy.GetParameterAsText(1)
Sort_X = arcpy.GetParameterAsText(2)
Sort_Y = arcpy.GetParameterAsText(3)
OutputFeature = arcpy.GetParameterAsText(4)

tempfea = InputFeature + str(time.time()).split('.')[0][-5:-1]

arcpy.CopyFeatures_management(InputFeature, tempfea)
arcpy.AddXY_management(tempfea)
if Order == '横向'.decode('UTF-8'):
    sortfield = [["POINT_Y", Sort_Y], ["POINT_X", Sort_X]]
elif Order == '纵向'.decode('UTF-8'):
    sortfield = [["POINT_X", Sort_X], ["POINT_Y", Sort_Y]]
arcpy.Sort_management(tempfea, OutputFeature, sortfield)
arcpy.AddField_management(OutputFeature, 'order1', 'DOUBLE')
arcpy.CalculateField_management(OutputFeature, 'order1', '!OBJECTID!', "PYTHON_9.3")
