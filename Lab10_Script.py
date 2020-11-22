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

import arcpy


def GetFeatures():
    
    featureClasses = arcpy.ListFeatureClasses()
    return featureClasses


def DefineProjections(shapefile_list, fcCount):
    known_sr_list = []
    unknown_sr_list = []
    new_sr = arcpy.GetParameterAsText(1)

    arcpy.SetProgressor("step", "Defining Projections...", 0, fcCount, 1)
    for item in shapefile_list:
        sr = arcpy.Describe(item).spatialReference
        if sr.name != "Unknown":
            known_sr_list.append(item)
        else:
            unknown_sr_list.append(item)
            sr = arcpy.DefineProjection_management(item, new_sr)
            arcpy.SetProgressorPosition()


    print("Known Projections: \n")
    for item in known_sr_list:
        sr = arcpy.Describe(item).spatialReference
        print("\t" + item + ": Spatial Reference known, reference is: " + sr.name)

    print("Unknown Projections: \n")
    for item in unknown_sr_list:
        sr = arcpy.Describe(item).spatialReference
        print("\t" + item + ": Spatial Reference unknown, defined projection to: " + sr.name)


arcpy.env.workspace = arcpy.GetParameterAsText(0)

feature_classes = GetFeatures()

feature_classes_count = len(feature_classes)

DefineProjections(feature_classes, feature_classes_count)
print("There are " + str(feature_classes_count) + " features in this workspace.")
print("Script Complete!")

