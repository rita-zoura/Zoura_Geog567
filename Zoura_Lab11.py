#--------------------------------------------------------------------
# Name: CSV to Feature with Statistics
# Author: Rita Zoura (UCID: 30018933)
# Created: 2020/11/28
#
# Purpose of script: Take a .csv file as input and output it as a shapefile,
#                    the user is also able to to store the resulting shapefile
#                    within a geodatabase. It preserves the original lat/long 
#                    coordinates in DMS, convert it to DD and adds it as new 
#                    attribute to the table. Also Releases statistics about the
#                    the file to the user in the geoprocessing details in ArcGIS Pro
#
# Inputs: Input table within a geodatabase that contains empty fields for Decimal Degrees 
#         for latitude adn longitude (Name them "DDLatitude" and "DDLongitude" for no errors). 
#         
#
# Outputs: It will fill the empty fields with the converted coordinates and also 
#          spit out statistics like, number of rows in the file, 
#          nortmost/southmost/westmost/eastmost/ coordinates and corresponding
#          observation ID's for those coordinates. Also the Percentage of 
#          observations that had a species presence
#
#--------------------------------------------------------------------

import arcpy

# Function to convert latitude coordinates from DMS to DD
# Input aprameters include the direction ("N or S"), latitudinal degree minutes
# and seconds seperate from each other
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
    # if latitude degrees is negative then
    if direction == "S":                                     
        lat_dd = lat_deg + lat_dec_min + lat_dec_sec
        # adds the negative back to ensure proper coordinate direction
        lat_dd = lat_dd * -1                            
    else:
        lat_dd = lat_deg + lat_dec_min + lat_dec_sec
    
    return lat_dd

# Function to convert longitude coordinates from DMS to DD
# Input aprameters include the direction ("W or E"), longitudinal degree minutes
# and seconds seperate from each other
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
    # if longitude degrees is west then
    if direction == "W":                                    
        long_dd = long_deg + long_dec_min + long_dec_sec
        # adds the negative to ensure proper coordinate direction
        long_dd = long_dd * -1                          
    else:
        long_dd = long_deg + long_dec_min + long_dec_sec

    # Prints the output values to the user as a string value
    return long_dd

# Get the table of coordinates from the user in ArcGIS Pro
csv_table = arcpy.GetParameterAsText(0)

# Selects the required fields that need to be converted from DMS and empty feilds to output the DD coords
fields = ["TxtLatitude", "TxtLongitude", "DDLatitude", "DDLongitude"]

# setup the search cursor
cursor = arcpy.da.UpdateCursor(csv_table, fields)

# go through each row
for row in cursor:
    try:
        # splite the text coordinates and assign them to their appropriate variable
        latitude = row[0].split("-")
        lat_direction = latitude[0]
        lat_deg = latitude[1]
        lat_min = latitude[2]
        lat_sec = latitude[3]

        # Use the latitude DMS to DD function to convert the coordinates and set it to the variable for reference
        lat_DD = lat_DMS_to_DD(lat_direction, lat_deg, lat_min, lat_sec)
        
        # split the tect coordinates and assign them to their appropriate variable
        longitude = row[1].split("-")
        long_direction = longitude[0]
        long_deg = longitude[1]
        long_min = longitude[2]
        long_sec = longitude[3]

        # Use the longitude DMS to DD fuction to conver the coordinates and set it to the variable for reference
        long_DD = long_DMS_to_DD(long_direction, long_deg, long_min, long_sec)
        
        # add the values from the variable to the appropriate row reference
        row[2] = lat_DD
        row[3] = long_DD
        
        # set the update to the table
        cursor.updateRow(row)
    except:
        arcpy.AddError("Error, no longitude/Latitude data to convert")
# deletes the cursor to prevent any errors
del cursor

# tells the user in the message center that the cooridnate conversion is complete
arcpy.AddMessage("DMS to DD conversion complete")

# Next Section gets the statistics for the file:

# Select new feilds for the new search cursor
stats_fields = ["Year", "ObservationID", "Presence", "DDLatitude", "DDLongitude"]

# Initiate the cursor with the new feild list
cursor = arcpy.da.SearchCursor(csv_table, stats_fields)

# initiate the row count
row_count = 0

# initiate whether there is a presence or not
presence = 0

# initiate the latitude and longitues value list
latitudes = []
longitudes = []

# go through each row in the curso and:
for row in cursor:
    # if there is a presence (presence == 1) then:
    if row[2] == 1:
        # add 1 to the presence count
        presence += 1
        # add the coordinates for that row to the lists for latitude and longitude
        latitudes.append(row[3])
        longitudes.append(row[4])

    # add plus 1 to the row count
    row_count += 1

# delete teh cursor to prevent errors
del cursor

# sort the latitudes list smallest to largets
latitudes.sort()
# assign the last one as the northmost latitude
north_lat = latitudes[-1]
# assign the first one as the southmost latitdude
south_lat = latitudes[0]

# sort the longitudes list smallest to largest
longitudes.sort()
# assign the first one to as the west most longitude
west_long = longitudes[0]
# assign the last one as the east most longitude
east_long = longitudes[-1]

# start a new cursor including the new query added to it. 
query = "Presence = 1"
cursor = arcpy.da.SearchCursor(csv_table, stats_fields, query)

# for every row in the cursor with a presence of 1
for row in cursor:
    try:
        # check if the north/south most latitude match the one in the row,
        # if so save the observation id
        if north_lat == row[3]:
            north_obser_id = row[1]
        if south_lat == row[3]:
            south_obser_id = row[1]
        # check if the west/east most longitudes match the one in the row,
        # if so save the observation id
        if west_long == row[4]:
            west_obser_id = row[1]
        if east_long == row[4]:
            east_obser_id = row[1]
    except:
        # if fails tell the user the error message
        arcpy.AddError("error no observation id found")
# delete the cursor for safety
del cursor

# out put the following statistics to teh user as messages in the geoprocessing details
arcpy.AddMessage("Northmost Latitude: {}, ObservationID: {}" .format(north_lat, north_obser_id))
arcpy.AddMessage("Southmost Latitude: {}, ObservationID: {}" .format(south_lat, south_obser_id))
arcpy.AddMessage("Westmost Longitude: {}, ObservationID: {}" .format(west_long, west_obser_id))
arcpy.AddMessage("Eastmost Longitude: {}, ObservationID: {}" .format(east_long, east_obser_id))

# calculate the rpesence percentage by divinding the the number of rows with a presence by the total
presence_percent = (presence / row_count) * 100
# display to user in geoprocessing details
arcpy.AddMessage("Presence Percentage: {}%" .format(presence_percent))
# tells the user the script is complete in the geoprocessing messages
arcpy.AddMessage("Script Complete!")