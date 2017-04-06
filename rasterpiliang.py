import arcpy
arcpy.env.workspace = "D:/test/NDVI"
savetif="D:/test/NDVI/cellstats.tif"
files=arcpy.ListRasters()
outCellStatistics = arcpy.gp.CellStatistics_sa(files,savetif,"MEDIAN", "NODATA")

