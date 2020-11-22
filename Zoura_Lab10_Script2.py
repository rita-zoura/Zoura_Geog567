#--------------------------------------------------------------------
# Name: Batch Projection Script       
# Author: Rita Zoura
# Created: 11/20/2020
# Use with ArcGIS Pro
#
# Purpose of script: To output to the user, the name, file type, and 
#                    dimensions of a raster file within a worspace,
#                    output the total number of bands within the workspace
#                    as well.
#
# Inputs: Workspace location
#
# Outputs: Outputs the information as a message to the user in geoprocessing
#          details.
#--------------------------------------------------------------------

# Imports Arcpy
import arcpy

# sets the workspace to the users input in arcGIS Pro
arcpy.env.workspace = arcpy.GetParameterAsText(0)

# Gets a list of rasters found in the workspace
rasters = arcpy.ListRasters()

# initializes how many bands there are
band_count = 0
# if there is at least one raster in the list
if len(rasters) > 0:
    # go through the list
    for raster in rasters:
        # decribe each raster in the list
        information = arcpy.Describe(raster)
        # if the file formate is a text based then remove it from the list
        if information.format == "AFR":
            rasters.remove(raster)
        
        # otherwise
        else:
            # get the name of the file
            name = information.name
            # get the file type it is
            file_type = information.format
            # get the number of rows
            height = information.height
            # get the number of columns
            width = information.width
            # does it contain a band
            has_band = information.bandCount
            # if it does
            if has_band > 0:
                # add plus 1 to the band count
                band_count += 1
        # output the information as messages to the user in geoporcessing
        # details
        arcpy.AddMessage("File " + name + ":")
        arcpy.AddMessage("\t file type: " + file_type)
        arcpy.AddMessage("\t dimensions: " + str(width) + " x " + str(height))
    # Tellthe user the number of raster bands in the workspace in geoprocessing details
    arcpy.AddMessage("There are " + str(band_count) + " bands in this folder")
# if there are no rasters in the workspace
else:
    # tell the user with an error that there are no rasters in the workspace.
    arcpy.AddError("There are no rasters in this workspace")