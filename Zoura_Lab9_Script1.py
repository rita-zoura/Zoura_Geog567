# Lab 7
# Rita Zoura | UCID: 30018933 | rita.zoura@ucalgary.ca
# Run using Python 3.6
# Vector script

import arcpy

def GetWorkspace():
    workspace = input("What is the location of the workspace folder?: ")
    return workspace

def GetFeatures(file_location):
    arcpy.env.workspace = workspace
    
    featureClasses = arcpy.ListFeatureClasses()
    return featureClasses


def DefineProjections(shapefile_list):
    known_sr_list = []
    unknown_sr_list = []
    new_sr = arcpy.SpatialReference("NAD 1983 UTM Zone 12N")

    for item in shapefile_list:
        sr = arcpy.Describe(item).spatialReference
        if sr.name != "Unknown":
            known_sr_list.append(item)
        else:
            unknown_sr_list.append(item)
            sr = arcpy.DefineProjection_management(item, new_sr)


    print("Known Projections: \n")
    for item in known_sr_list:
        sr = arcpy.Describe(item).spatialReference
        print("\t" + item + ": Spatial Reference known, reference is: " + sr.name)

    print("Unknown Projections: \n")
    for item in unknown_sr_list:
        sr = arcpy.Describe(item).spatialReference
        print("\t" + item + ": Spatial Reference unknown, defined projection to: " + sr.name)


workspace = GetWorkspace()

feature_classes = GetFeatures(workspace)

feature_classes_count = len(feature_classes)

DefineProjections(feature_classes)
print("There are " + str(feature_classes_count) + " features in this workspace.")
print("Script Complete!")

