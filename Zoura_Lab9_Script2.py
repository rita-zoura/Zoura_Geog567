# Lab 7
# Rita Zoura | UCID: 30018933 | rita.zoura@ucalgary.ca
# Run using Python 3.6
# Raster script

import arcpy

workspace = input("What is the location of your workspace folder?: ")
arcpy.env.workspace = workspace

rasters = arcpy.ListRasters()

for raster in rasters:
    info = arcpy.Describe(raster)
    name = info.name
    file_type = info.format



