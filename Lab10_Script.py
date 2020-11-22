#--------------------------------------------------------------------
# Name: Batch Projection Script       
# Author: Rita Zoura
# Created: 11/20/2020
#
# Purpose of script: To define the projection of any shapfiles 
#                    in the workspace that dont already have one
#                    user can choose a spatial reference of choice.
#
# Inputs: Workspace location and Spatial Reference
#
# Outputs: Outputs the newly projected files to the same workspace as the 
#          original input workspace.
#--------------------------------------------------------------------


# imorts arcpy to use arcpy functions in the script
import arcpy

# Function to get the features from the wrokspace as a list.
# returns a list of the feature classes. No parameter required
def GetFeatures():
    
    featureClasses = arcpy.ListFeatureClasses()
    return featureClasses

# Function to define the projection of shapefiles within the list that dont already have a projection.
# returns nothing
# Parameters required: 
#   a list of shapefiles
#   the number of shapefiles in the list
def DefineProjections(shapefile_list, fcCount):
    # initialize lists to keep track of shapfiles with known projections an dunknow projections
    # seperate from each other.
    known_sr_list = []
    unknown_sr_list = []
    # let the user pick what projection they want to define unknown projections to
    new_sr = arcpy.GetParameterAsText(1)

    # sets the step progressor
    arcpy.SetProgressor("step", "Defining Projections...", 0, fcCount, 1)

    # loops through each item in the list of shapefiles
    for item in shapefile_list:
        # What is the current spatial reference for this shapefile
        sr = arcpy.Describe(item).spatialReference

        # if the shapefile has a spatial reference that inst labelled as "unknown"
        if sr.name != "Unknown":

            # add that shapefile to the list of shpaefiles with known projections
            known_sr_list.append(item)
        
        # otherwise
        else:
            # add this shapefile to the list of shapfiles with an "unknown" projection
            unknown_sr_list.append(item)
            
            # Define the projection to the spatial reference defined by the user
            sr = arcpy.DefineProjection_management(item, new_sr)
            # Set the progressor to move the next step.
            arcpy.SetProgressorPosition()

    # Print out the following information to the user as a message in Geoprocessing Details
    arcpy.AddMessage("Known Projections: \n")
    # goes through the shapefiles with known projections
    for item in known_sr_list:
        # gets the known spatial reference for this shapefile
        sr = arcpy.Describe(item).spatialReference
        # send a message to the user
        arcpy.AddMessage("\t" + item + ": Spatial Reference known, reference is: " + sr.name)

    # Print out the following information to the user as a message in geoprocessing details
    arcpy.AddMessage("Unknown Projections: \n")
    # goes throught he shapefiles with unknown projections
    for item in unknown_sr_list:
        # gets the newly defined spatial reference of the shapefiles
        sr = arcpy.Describe(item).spatialReference
        # sends a message to the user
        arcpy.AddMessage("\t" + item + ": Spatial Reference unknown, defined projection to: " + sr.name)

# sets teh workspace environemnt as input from user in ArcGIS Pro
arcpy.env.workspace = arcpy.GetParameterAsText(0)

# Gets the list of al the shapefiles in the workspace
feature_classes = GetFeatures()

# Gets the number of shapefiles found in the workspace
feature_classes_count = len(feature_classes)

# Performs the 'DefineProjections()' function
DefineProjections(feature_classes, feature_classes_count)
# Sends a message to the user in the geoprocessing details in ArcGIS Pro
arcpy.AddMessage("There are " + str(feature_classes_count) + " features in this workspace.")
# tells the user script has finished in geoprocessing details in ArcGIS pro
arcpy.AddMessage("Script Complete!")

