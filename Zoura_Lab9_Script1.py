# Lab 7
# Rita Zoura | UCID: 30018933 | rita.zoura@ucalgary.ca
# Run using Python 3.6
# Vector script

import arcpy

workspace = input("What is the location of the workspace folder?: ")

arcpy.env.workspace = workspace

featureClasses = arcpy.ListFeatureClasses()


known_sr_list = []
unknown_sr_list = []


new_sr = arcpy.SpatialReference("NAD 1983 UTM Zone 12N")

for fc in featureClasses:
    sr = arcpy.Describe(fc).spatialReference
    if sr.name != "Unknown":
        known_sr_list.append(fc)
    else:
        unknown_sr_list.append(fc)
        sr = arcpy.DefineProjection_management(fc, new_sr)

print("Known Projections: \n")
for fc in known_sr_list:
    sr = arcpy.Describe(fc).spatialReference
    print("\t" + fc + ": Spatial Reference known, reference is: " + sr.name)

print("Unknown Projections: \n")
for fc in unknown_sr_list:
    sr = arcpy.Describe(fc).spatialReference
    print("\t" + fc + ": Spatial Reference unknown, defined projection to: " + sr.name)

