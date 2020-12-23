# Lab 6
# Rita Zoura | UCID: 30018933 | rita.zoura@ucalgary.ca
# Run using Python 3.6

# This script is meant to take LiDAR15 DEM .xyz files and output the following:
#   1. The number of points
#   2. The lower-left coordinates
#   3. The upper-right coordinates
#   4. The minimum elevation
#   5. The maximum elevation
#   6. The approximate tile size in kilometers (length x height)

# Asks the user to input the file
filename = str(input("What is the file location of the ArcInfo ASCII raster file using forward slashes? \n(Must be a .xyz file ex. C:/LiDAR15/DEM.xyz): "))
file = open(filename, "r")

# Split the file so that each set of X, Y, Z coordinates is on one line
coordinates = file.readlines()
line_count = 0

for line in coordinates:
    line_count += 1         


coord_line = line.split()               # Splits the line of coordinates so that they are seperate

min_easting = float(coord_line[0])      # Sets the first set of coordinates to the min/max variables for
max_easting = float(coord_line[0])      # easting, northing and elevation to initialize the variables

min_northing = float(coord_line[1])
max_northing = float(coord_line[1])

min_elevation = float(coord_line[2])
max_elevation = float(coord_line[2])


for line in coordinates:                            # Loops through each line of coordinates
    coord_line = line.split()                       # and splits each line so the values are seperate
    
    for coord in coord_line:                        # Loops through each seperate value in the line of coordinates

        if float(coord_line[0]) < min_easting:      # If the min_easting in the new line is less than the 
            min_easting = float(coord_line[0])      # original then replace min_easting wtih the lower value
        
        elif float(coord_line[0]) > max_easting:    # If the max_easting in the new line is less than the
            max_easting = float(coord_line[0])      # orignal then replace the max_easting with larger value
        
        elif float(coord_line[1]) < min_northing:   # If the min_northing in the new line is less than the
            min_northing = float(coord_line[1])     # orignal then replace the min_northing with the lower value
        
        elif float(coord_line[1]) > max_northing:   # If the max_northing in the in the new line is less than the
            max_northing = float(coord_line[1])     # orignal then replace the max_northing with the larger value
        
        elif float(coord_line[2]) < min_elevation:  # If the min_elevation in the new line is less than the 
            min_elevation = float(coord_line[2])    #original then replace the min_elevation with the lower value
        
        elif float(coord_line[2]) > max_elevation:  # If the max_elevation in the new line is less than the 
            max_elevation = float(coord_line[2])    # original then replace the max_elevation with the larger value

# Find the size of the tile and convert the values to kilometers
tile_length = (max_easting - min_easting) / 1000
tile_height = (max_northing - min_northing) / 1000

# Outputs all the information to the user:
print("Number of points: " + str(line_count)) # Outputs the number of points

print("Lower-left coordinate: UTM (6TM) " + str(min_easting) + " E " + str(min_northing) + " N")    # Outputs the 
                                                                                                    # lower-left coordinate

print("Upper-right coordinate: UTM (6TM) " + str(max_easting) + " E " + str(max_northing) + " N")   # Outputs the 
                                                                                                    # upper-right coordinate      

print("Minimum elevation: " + str(min_elevation) + " m")   # Outputs the minimum elevation
print("Maximum elevation: " + str(max_elevation) + " m")   # Outputs the maximum elevation

print("Tile size: " + str(tile_length) + " km x " + str(tile_height) + " km")  # Outputs the tile size 

file.close() # Closes the file.