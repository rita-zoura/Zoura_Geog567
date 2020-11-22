# Lab 9
# Rita Zoura | UCID: 30018933 | rita.zoura@ucalgary.ca
# Run using Python 3.6
# Vector script

# Import arcpy
import arcpy

# function to get the workspace from the user
# no parameters
def GetWorkspace():
    workspace = input("What is the location of the workspace folder?: ")
    # returns the workspace location
    return workspace

# function to get the list of features and set the workspace location
def GetFeatures(file_location):
    # Sets the workspace
    arcpy.env.workspace = workspace
    
    # list of feature calsses in the workspace
    featureClasses = arcpy.ListFeatureClasses()

    # returns the list of feature calsses found in the workspace
    return featureClasses

# function defines projections for shapefiles missing prjection information.
# outputs the information to the user in the terminal
# if a shapefiel contains a spatial reference then it prints it to the terminal
# if the shapfile doens not it difeines the projection to NAD 193 UTM Zone 12N 
# and print it to the terminal and user.
def DefineProjections(shapefile_list):
    # initialize list of fiels with known spatial reference
    known_sr_list = []
    # initializes list of files with unknown spatial reference
    unknown_sr_list = []

    # sets a new spatial reference to NAD 1983 UTM Zone 12N
    new_sr = arcpy.SpatialReference("NAD 1983 UTM Zone 12N")

    # goes through the list and
    for item in shapefile_list:
        # describes the spatial reference of the file
        sr = arcpy.Describe(item).spatialReference
        # if it isn't "unknown"
        if sr.name != "Unknown":
            # then it gets added the list of fiels with knwon spatial references
            known_sr_list.append(item)
        
        # otherwise
        else:
            # the fiel gets added to the list of files with unknown spatial references
            unknown_sr_list.append(item)
            # and the spatialreference is defined to NAD 1983 UTM Zone 12N
            sr = arcpy.DefineProjection_management(item, new_sr)

    # Output the information about to the user in an orginized matter
    print("Known Projections: \n")
    for item in known_sr_list:
        sr = arcpy.Describe(item).spatialReference
        print("\t" + item + ": Spatial Reference known, reference is: " + sr.name)

    print("Unknown Projections: \n")
    for item in unknown_sr_list:
        sr = arcpy.Describe(item).spatialReference
        print("\t" + item + ": Spatial Reference unknown, defined projection to: " + sr.name)

# activates getWorkspace function
workspace = GetWorkspace()

# activates get features function
feature_classes = GetFeatures(workspace)

# gets the number of features in the workspace
feature_classes_count = len(feature_classes)

# Activates teh define projection function
DefineProjections(feature_classes)

# prints the following to the user.
print("There are " + str(feature_classes_count) + " features in this workspace.")
print("Script Complete!")

