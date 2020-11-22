# Lab 7
# Rita Zoura | UCID: 30018933 | rita.zoura@ucalgary.ca
# Run using Python 3.6
# Raster script

# Imports Arcpy
import arcpy

# Gets the workspace location from the user
workspace = input("What is the location of your workspace folder?: ")
# sets the workspace
arcpy.env.workspace = workspace

# gets a list of rasters in workspace
rasters = arcpy.ListRasters()
# initializes number of bands in workspace
band_count = 0
# go throug heach raster in list
for raster in rasters:
    # describe the raster
    information = arcpy.Describe(raster)
    # if the format is text based
    if information.format == "AFR":
        # remove it from the list
        rasters.remove(raster)
    # otherwise
    else:
        # get the name
        name = information.name
        # get teh file type
        file_type = information.format
        # get teh number of rows
        height = information.height
        # get the number of columns
        width = information.width
        # does it contain a band
        has_band = information.bandCount
        # if it does at plus 1 to the band count
        if has_band > 0:
            band_count += 1
    
    # out the information neatly to user in the terminal
    print("File " + name + ":")
    print("\t file type: " + file_type)
    print("\t dimensions: " + str(width) + " x " + str(height))

# output the number of bunds int he workspace to the user
print("There are " + str(band_count) + " bands in this folder")