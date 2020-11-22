#--------------------------------------------------------------------
# Name: Batch Projection Script       
# Author: Rita Zoura
# Created: 11/20/2020
#
# Purpose of script: To output to the user, the name, file type, and 
#                    dimensions of a raster file within a worspace,
#                    output the total number of bands within the workspace
#                    as well.
#
# Inputs: Workspace location
#
# Outputs: Outputs the information as a message to the user.
#--------------------------------------------------------------------

import arcpy

arcpy.env.workspace = arcpy.GetParameterAsText(0)

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
    arcpy.AddMessage("File " + name + ":")
    arcpy.AddMessage("\t file type: " + file_type)
    arcpy.AddMessage("\t dimensions: " + str(width) + " x " + str(height))

arcpy.AddMessage("There are " + str(band_count) + " bands in this folder")