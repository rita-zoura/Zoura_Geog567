# Lab 7
# Rita Zoura | UCID: 30018933 | rita.zoura@ucalgary.ca
# Run using Python 3.6
# Vector script

import arcpy

def GetWorkspace():
    workspace = input("What is the location of the workspace folder?: ")
    return workspace

# def GetShapefiles():
#     shapefiles = arcpy.ListFeatureClasses()
#     return shapefiles

def GetKnownProjection():
    known_sr_list = []
    shapefiles = arcpy.ListFeatureClasses()
    for feature in shapefiles:
        sr = arcpy.Describe(feature).spatialReference
        
        if sr.name != "Unknown":
            feature.append(known_sr_list)
        
    return known_sr_list

def GetUnknownProjection():
    unknown_sr_list = []
    shapefiles = arcpy.ListFeatureClasses()
    for feature in feature_class_list:
        sr = arcpy.Describe(feature).spatialReference
        if sr.name == "Unknown":
            feature.append(unknown_sr_list)
    
    return unknown_sr_list

def DefineProjectionToNAD193UTMZone12N(feature_class_list):
    coord_sys = arcpy.SpatialReference("NAD 1983 UTM Zone 12N")
    
    for feature in feature_class_list:
        spatial_ref = arcpy.Describe(feature).spatialReference
        spatial_ref = arcpy.DefineProjection_management(feature, coord_sys)
        
        return spatial_ref



# new_sr = arcpy.SpatialReference("NAD 1983 UTM Zone 12N")


# for fc in shapefiles:
#     sr = arcpy.Describe(fc).spatialReference
#     if sr.name != "Unknown":
#         fc.append(known_sr_list)
#     else:
#         fc.append(unknown_sr_list)




# sr = arcpy.DefineProjection_management(fc, new_sr)


arcpy.env.workspace = GetWorkspace()

known_projections = GetKnownProjection()
unknown_projections = GetUnknownProjection()

for item in unknown_projections:
    new_sr = DefineProjectionToNAD193UTMZone12N(unknown_projections)
    print(new_sr)

# for item in known_projections:
#     sr = arcpy.Describe(item).spatialReference
#     print(sr)

