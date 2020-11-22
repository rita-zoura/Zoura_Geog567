# Lab 7
# Rita Zoura | UCID: 30018933 | rita.zoura@ucalgary.ca
# Run using Python 3.6
# Raster script

import arcpy

workspace = input("What is the location of your workspace folder?: ")
arcpy.env.workspace = workspace

rasters = arcpy.ListRasters()

band_count = 0

for raster in rasters:
    information = arcpy.Describe(raster)
    if information.format == "AFR":
        rasters.remove(raster)
    else:
        name = information.name
        file_type = information.format
        height = information.height
        width = information.width
        has_band = information.bandCount
        if has_band > 0:
            band_count += 1
    print("File " + name + ":")
    print("\t file type: " + file_type)
    print("\t dimensions: " + str(width) + " x " + str(height))

print("There are " + str(band_count) + " bands in this folder")