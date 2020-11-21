# Lab 7
# Rita Zoura | UCID: 30018933 | rita.zoura@ucalgary.ca
# Run using Python 3.6
# Raster script

import arcpy

workspace = input("What is the location of your workspace folder?: ")
arcpy.env.workspace = workspace

rasters = arcpy.ListRasters()

for raster in rasters:
    information = arcpy.Describe(raster)
    name = information.name
    height = information.height
    width = information.width
    file_typee = information.format
    print(name, width, height, file_typee)



