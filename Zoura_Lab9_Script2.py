# Lab 7
# Rita Zoura | UCID: 30018933 | rita.zoura@ucalgary.ca
# Run using Python 3.6
# Raster script

import arcpy

workspace = input("What is the location of your workspace folder?: ")
arcpy.env.workspace = workspace

rasters = arcpy.ListRasters()

for raster in rasters:
    name = arcpy.Describe(raster).name
    file_type = arcpy.Describe(raster).format
    width = arcpy.Describe(raster).width

    print(name, file_type, width)




