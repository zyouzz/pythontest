#!/usr/bin/env python
# -*-coding:utf-8 -*-
__author__ = 'jiang'
'''****************************************************************************
 Name:         Sun Sky Map
 Description:  The following script creates point feature(s) that model the
               sun's position (azimuth and angle) from the centroid of the
               input feature class. The equations used for determining sun
               position are provided by PyEphem, a scientific grade astronomical
               computation module developed for Python available here:
               http://rhodesmill.org/pyephem/index.html
 Requirements: - ArcGIS 10.0
               - Python 2.6
               - PyEphem
 Author:       Khalid Duri, ESRI
***************************************************************************'''

import arcpy, ephem
import datetime, time
import exceptions, os, traceback, sys
from arcpy import env
from math import radians, degrees, pi, sin, cos, tan
from datetime import datetime, time, timedelta
from time import strptime

# ****************************  Script Variables  ******************************
inFC = arcpy.GetParameterAsText(0)  # input feature class
inTimeZone = arcpy.GetParameterAsText(1)  # time zone
startDate = arcpy.GetParameterAsText(2)  # starting date
endDate = arcpy.GetParameterAsText(3)  # ending date
dayInterval = arcpy.GetParameter(4)  # day interval
hrInterval = arcpy.GetParameter(5)  # hour interval
minInterval = arcpy.GetParameter(6)  # minute interval
enforceTime = arcpy.GetParameter(7)  # minute interval
outSun = arcpy.GetParameterAsText(8)  # output sun features
distance = arcpy.GetParameter(9)  # sun model's distance
horizonElevation = arcpy.GetParameter(10)  # average elevation of area of interest

timezone = {
    '(UTC-12:00) International Date Line West': -12,
    '(UTC-11:00) Midway Island, Samoa': -11,
    '(UTC-10:00) Hawaii': -10,
    '(UTC-9:00) Alaska': -9,
    '(UTC-8:00) Pacific Time (US & Canada), Baja California': -8,
    '(UTC-7:00) Mountain Time (US & Canada), Chihuahua, La Paz, Mazatlan': -7,
    '(UTC-6:00) Central Time (US & Canada), Central America, Guadalajara,' \
    ' Mexico City': -6,
    '(UTC-5:00) Eastern Time (US & Canada), Bogota, Lima, Quito': -5,
    '(UTC-4:00) Atlantic Time (Canada), Santiago, La Paz, San Juan': -4,
    '(UTC-3:30) Newfoundland (Canada)': -3.5,
    '(UTC-3:00) Brasilia, Buenos Aires, Cayenne, Greenland, Montevideo': -3,
    '(UTC-2:00) Mid-Atlantic': -2,
    '(UTC-1:00) Cape Verde Islands, Azores': -1,
    '(UTC) Casablanca, Dublin, Edinburgh, London, Monrovia': 0,
    '(UTC+1:00) West Central Africa, Amsterdam, Berlin, Rome, Sarajevo,' \
    ' Stockholm': 1,
    '(UTC+2:00) Amman, Athens, Beirut, Cairo, Harare, Helsinki, Istanbul,' \
    ' Pretoria': 2,
    '(UTC+3:00) Kuwait, Baghdad, Moscow, Nairobi, Riyadh': 3,
    '(UTC+3:30) Tehran': 3.5,
    '(UTC+4:00) Abu Dhabi, Baku, Muscat, Tbilisi, Yerevan': 4,
    '(UTC+5:00) Ekaterinburg. Islamabad, Karachi, Tashkent': 5,
    '(UTC+5:30) Chennai, Kolkata, Mumbai, New Delhi': 5.5,
    '(UTC+6:00) Astana, Dhaka, Novosibirsk': 6,
    '(UTC+7:00) Bangkok, Hanoi, Jakarta': 7,
    '(UTC+8:00) Beijing, Hong Kong, Kuala Lampur, Singapore, Taipei,' \
    ' Ulaanbaatar': 8,
    '(UTC+9:00) Osaka, Seoul, Tokyo, Yakutsk': 9,
    '(UTC+9:30) Adelaide, Darwin': 9.5,
    '(UTC+10:00) Brisbane, Melbourne, Guam, Bladivostok': 10,
    '(UTC+11:00) Magadan, Solomon Islands': 11,
    '(UTC+12:00) Fiji, Marshall Islands': 12
}


# **************************  Script Error Trapper  ****************************
class CustomError(Exception):
    def __init__(self, value):
        self.parameter = value

    def __str__(self):
        return repr(self.parameter)


# ****************************  Script Functions  ******************************

class ObservationPoint:
    def __init__(self):
        # Get centroid of input for observer location
        desc = arcpy.Describe(inFC)
        sourceSR = desc.spatialReference
        newSR = arcpy.SpatialReference()
        newSR.factoryCode = sourceSR.factoryCode
        newSR.create()
        self.SR = newSR
        self.X = desc.extent.XMin + ((desc.extent.XMax - desc.extent.XMin) / 2)
        self.Y = desc.extent.YMin + ((desc.extent.YMax - desc.extent.YMin) / 2)
        self.ObservationPoint()

    def ObservationPoint(self):
        # Create in memory observation point
        obsPt = arcpy.CreateUniqueName('temp', 'in_memory')
        arcpy.management.CreateFeatureclass('in_memory', obsPt.split(os.sep)[-1],
                                            'POINT', '', '', 'ENABLED', self.SR)
        # Add field to store True North offset calculation
        arcpy.management.AddField(obsPt, 'TrueNorth', 'DOUBLE')

        # Load centroid into in-memory layer
        addObsPt = arcpy.InsertCursor(obsPt)
        obsCentroid = addObsPt.newRow()
        obsCentroid.Shape = arcpy.Point(self.X, self.Y)
        obsCentroid.TrueNorth = 0
        addObsPt.insertRow(obsCentroid)
        del addObsPt, obsCentroid

        # Calculated True North offset for projected SR
        if self.SR.type == 'Projected':
            # Determine projection offset
            arcpy.cartography.CalculateGridConvergenceAngle(obsPt, 'TrueNorth')

        # Get observer point in longitude & latitude
        SR = "GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984'," \
             "6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree'," \
             "0.0174532925199433]]"
        rows = arcpy.SearchCursor(obsPt, '', SR)
        row = rows.next()
        self.lon = row.Shape.centroid.X
        self.lat = row.Shape.centroid.Y
        self.trueNorthOffset = row.TrueNorth
        del rows, row
        arcpy.management.Delete(obsPt)


class Times():
    def __init__(self):
        self.Times = []
        if startDate.endswith('M'):
            startLocal = datetime.strptime(startDate, "%m/%d/%Y %I:%M:%S %p")
        else:
            startLocal = datetime.strptime(startDate, "%m/%d/%Y %H:%M:%S")
        if endDate:  # Defines behavior when end date is supplied
            if endDate.endswith('M'):
                endLocal = datetime.strptime(endDate, "%m/%d/%Y %I:%M:%S %p")
            else:
                endLocal = datetime.strptime(endDate, "%m/%d/%Y %H:%M:%S")
            if dayInterval or hrInterval or minInterval:
                if enforceTime:  # Defines behavior when Enforce Time is enabled
                    initial = startLocal
                    while startLocal < endLocal:
                        if initial.time() <= startLocal.time() <= endLocal.time():
                            self.Times.append(startLocal)
                        startLocal += timedelta(days=dayInterval, hours=hrInterval,
                                                minutes=minInterval)
                    self.Times.append(endLocal)
                else:  # Defines the behavior when Enforce Time is disabled
                    while startLocal < endLocal:
                        self.Times.append(startLocal)
                        startLocal += timedelta(days=dayInterval, hours=hrInterval,
                                                minutes=minInterval)
                    self.Times.append(endLocal)
            else:  # Use first and last dates when no interval is provided
                self.Times.extend([startLocal, endLocal])
        else:  # Behavior when end date is not given
            daymonthyear = datetime.date(startLocal)
            if dayInterval:
                while startLocal <= datetime(daymonthyear.year, 12, 31, 23, 59):
                    self.Times.append(startLocal)
                    startLocal += timedelta(days=dayInterval, hours=hrInterval,
                                            minutes=minInterval)
            elif hrInterval or minInterval:  # When only hour or min interval are given
                while datetime.date(startLocal) == daymonthyear:
                    self.Times.append(startLocal)
                    startLocal += timedelta(hours=hrInterval, minutes=minInterval)
            else:  # Behavior when no interval is given
                self.Times.append(startLocal)
        self.UTC_Correction()

    def UTC_Correction(self):
        for dt in self.Times:
            dtPosition = self.Times.index(dt)
            self.Times[dtPosition] = dt - timedelta(hours=timezone[inTimeZone])


class SunCalculation():
    def __init__(self, timeList, lon, lat, X, Y):
        sunPos = ephem.Observer()
        sunPos.long, sunPos.lat = str(lon), str(lat)
        sun = ephem.Sun()
        # utc_correction = timezone[inTimeZone]*ephem.hour
        self.SunPosition = {}
        self.SunTimes = []
        for dt in timeList:
            # sunPos.date = ephem.Date(ephem.Date(dt) - utc_correction)
            sunPos.date = ephem.Date(ephem.Date(dt))
            sun.compute(sunPos)
            print
            sun.alt
            if sun.alt > 0:
                self.SunPosition[dt] = (sun.alt, sun.az)
                self.SunTimes.append(dt)
        if self.SunTimes:
            self.SkyMapCoordinates(X, Y)
        else:
            raise CustomError('There are no daylight times for the specified arguments.')

    def SkyMapCoordinates(self, X, Y):
        self.ZMax = -99999
        for SunTime in self.SunTimes:
            angle = self.SunPosition[SunTime][0]
            azimuth = self.SunPosition[SunTime][1]
            # Identify quadrant in XY space
            quad = int((2 * azimuth) / pi)
            # Returns the appropriate complementary angle for quadratic formula
            AZoffset = azimuth - (pi / 2) * quad
            # Quad 0 is the first quadrant, 1 is the second, 2 is third, 3 is fourth
            if quad == 0:
                x = X + distance * sin(AZoffset)
                y = Y + distance * cos(AZoffset)
            elif quad == 1:
                x = X + distance * cos(AZoffset)
                y = Y - distance * sin(AZoffset)
            elif quad == 2:
                x = X - distance * sin(AZoffset)
                y = Y - distance * cos(AZoffset)
            elif quad == 3:
                x = X - distance * cos(AZoffset)
                y = Y + distance * sin(AZoffset)
            z = int(horizonElevation + distance * tan(angle))
            if z > self.ZMax:
                self.ZMax = z
            self.SunPosition[SunTime] = (degrees(azimuth), degrees(angle),
                                         x, y, z)


class CreateSkymap():
    def __init__(self, SR, zMax=0, SunTimes=[], SunPosition={}):
        outPath = outSun.replace('{0}{1}'.format(os.sep, outSun.split(os.sep) \
            [len(outSun.split(os.sep)) - 1]), '')
        outName = outSun.split(os.sep)[len(outSun.split(os.sep)) - 1]
        env.ZDomain = '-1000000 {0}'.format(zMax)
        arcpy.CreateFeatureclass_management(outPath, outName, 'POINT', '',
                                            '', 'ENABLED', SR)
        if arcpy.Describe(outSun).dataType == 'ShapeFile':
            arcpy.AddField_management(outSun, 'LOCAL_TIME', 'TEXT')
            arcpy.DeleteField_management(outSun, 'Id')
        else:
            arcpy.AddField_management(outSun, 'LOCAL_TIME', 'DATE')
        arcpy.AddField_management(outSun, 'AZIMUTH', 'DOUBLE')
        arcpy.AddField_management(outSun, 'ANGLE', 'DOUBLE')
        self.LoadSunPoints(SunTimes, SunPosition)

    def LoadSunPoints(self, SunTimes=[], SunPosition={}):
        addSunPts = arcpy.InsertCursor(outSun)
        for SunTime in SunTimes:
            SunPosition[SunTime]
            sunPt = addSunPts.newRow()
            sunPt.Shape = arcpy.Point(SunPosition[SunTime][2],
                                      SunPosition[SunTime][3],
                                      SunPosition[SunTime][4])
            sunPt.LOCAL_TIME = SunTime
            sunPt.AZIMUTH = round(SunPosition[SunTime][0], 2)
            sunPt.ANGLE = round(SunPosition[SunTime][1], 2)
            addSunPts.insertRow(sunPt)
        del addSunPts


'''****************************************************************************
******************************  Begin Execution  ******************************
****************************************************************************'''
try:
    obs = ObservationPoint()
    timeList = Times().Times
    sc = SunCalculation(timeList, obs.lon, obs.lat, obs.X, obs.Y)
    CreateSkymap(obs.SR, sc.ZMax, sc.SunTimes, sc.SunPosition)
except CustomError, (instance):
    arcpy.AddError('Error: {0}'.format(instance.parameter))
except arcpy.ExecuteError:
    print
    arcpy.GetMessages()
except:
    # Get the traceback object
    tb = sys.exc_info()[2]
    tbinfo = traceback.format_tb(tb)[0]
    # Concatenate error information into message string
    pymsg = 'PYTHON ERRORS:\nTraceback info:\n{0}\nError Info:\n{1}' \
        .format(tbinfo, str(sys.exc_info()[1]))
    msgs = 'ArcPy ERRORS:\n {0}\n'.format(arcpy.GetMessages(2))
    # Return python error messages for script tool or Python Window
    arcpy.AddError(pymsg)
    arcpy.AddError(msgs)