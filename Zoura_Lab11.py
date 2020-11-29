#--------------------------------------------------------------------
# Name: CSV to Feature with Statistics
# Author: Rita Zoura (UCID: 30018933)
# Created: 2020/11/28
#
# Purpose of script: Take a .csv file as input and output it as a shapefile,
#                    the user is also able to to store the resulting shapefile
#                    within a geodatabase. It preserves the original lat/long 
#                    coordinates in DMS, convert it to DD and adds it as new 
#                    attribute to the table.
#
# Inputs:
#
# Outputs:
#
#--------------------------------------------------------------------

import arcpy

def lat_DMS_to_DD(direction, latitudinal_degrees, latitudinal_minutes, latitudinal_seconds):
    # Input the values for the latitudinal degrees, minutes and seconds seperately
    lat_deg = float(latitudinal_degrees)
    lat_min = float(latitudinal_minutes)
    lat_sec = float(latitudinal_seconds)
    
    # Convert latitudinal minutes to decimals
    lat_dec_min = lat_min / 60
    # Convert latitudinal seconds to decimals
    lat_dec_sec = lat_sec / 3600
    
    # Add latitudinal decimal values to latitudinal degrees
    if direction == "S":                                     # if latitude degrees is negative then
        lat_dd = lat_deg + lat_dec_min + lat_dec_sec
        lat_dd = lat_dd * -1                            # adds the negative back to ensure proper coordinate direction
    else:
        lat_dd = lat_deg + lat_dec_min + lat_dec_sec
    
    return lat_dd

def long_DMS_to_DD(direction, longitudinal_degrees, longitudinal_minutes, longitudinal_seconds):

    # Input the value for the longitudinal degrees, minutes, seconds seperately
    long_deg = float(longitudinal_degrees)
    long_min = float(longitudinal_minutes)
    long_sec = float(longitudinal_seconds)

    # Convert longitudinal minutes to decimals
    long_dec_min = long_min / 60
    # Convert longitudinal seconds to decimals
    long_dec_sec = long_sec / 3600

    # Add longitudinal decimal values to longitudinal degrees
    if direction == "W":                                    # if longitude degrees is west then
        long_dd = long_deg + long_dec_min + long_dec_sec
        long_dd = long_dd * -1                          # adds the negative to ensure proper coordinate direction
    else:
        long_dd = long_deg + long_dec_min + long_dec_sec

    # Prints the output values to the user as a string value
    return long_dd

# def GetStatistics(in_file):

#     cursor = arcpy.da.SearchCursor(in_file, "*")
#     row_count = 0
#     for row in cursor:
#         row_count += 1
        
    # Total number of observations in the feature class.
    

    # Percentage of observations that indicated the species was present.
    # The latitudes and ObservationID values of the northmost and southmost
    # observations (note: an observation is indicated when the Presence field = 1).
    # The longitudes and ObservationID values of the westmost and eastmost
    # observations


# csv_table = arcpy.GetParameterAsText(0)

# fields = ["TxtLatitude", "TxtLongitude", "DDLatitude", "DDLongitude"]

# cursor = arcpy.da.UpdateCursor(csv_table, fields)

# for row in cursor:
#     latitude = row[0].split("-")
#     lat_direction = latitude[0]
#     lat_deg = latitude[1]
#     lat_min = latitude[2]
#     lat_sec = latitude[3]

#     lat_DD = lat_DMS_to_DD(lat_direction, lat_deg, lat_min, lat_sec)
    
#     longitude = row[1].split("-")
#     long_direction = longitude[0]
#     long_deg = longitude[1]
#     long_min = longitude[2]
#     long_sec = longitude[3]

#     long_DD = long_DMS_to_DD(long_direction, long_deg, long_min, long_sec)
    
#     row[2] = lat_DD
#     row[3] = long_DD
    
#     cursor.updateRow(row)

# del cursor

# arcpy.AddMessage("DMS to DD conversion complete")

file = "E:/GEOG_567/Lab_11/MyProject2/MyProject2.gdb/coords_DD"

stats_fields = ["Year", "ObservationID", "Presence", "DDLatitude", "DDLongitude"]

stats_cursor = arcpy.da.SearchCursor(file, stats_fields)

row_count = 0

presence = 0
no_presence = 0

north_lat = 0
south_lat = 0

west_long = 0
east_long = 0

for row in stats_cursor:
    row_count += 1
    
    if row[2] == 1:
        presence += 1
    else:
        no_presence += 1

presence_percent = (presence / row_count) * 100


