# Lab 7
# Rita Zoura | UCID: 30018933 | rita.zoura@ucalgary.ca
# Run using Python 3.6

# This script creates the class LiDAR15DEM which contains the following properties:
#   1. The number of points
#   2. The lower-left coordinates
#   3. The upper-right coordinates
#   4. The minimum elevation
#   5. The maximum elevation
#   6. Width of the tile
#   7. Height of the tile
# And the following methods:
#   1. __init__
#   2. open()
#   3. outputStatistics()

# Create the class LiDAR15DEM
class LiDAR15DEM:
    # Initialize the properties for the class. 
    def __init__(self):
        # Number of Points
        self.numPoints = 0
        # Lower-left coordinate
        self.LLcoord = []
        # Upper-right coordinate
        self.URcoord = []
        # Tile width
        self.width = 0
        # Tile height
        self.height = 0
        # Minimum elevation
        self.minElev = 0
        # Maximum elevation
        self.maxElev = 0

    def open(self, fileInput):
        # Opens the file at the location of fileInput and reads it
        file = open(fileInput, "r")

        # Reads through each line in the file
        coordinates = file.readlines()
        line_count = 0

        # Loops through each line in the file and adds to the line_count
        for line in coordinates:
            line_count += 1
        
        # Splits the line of coordinates so that they are seperate
        coord_line = line.split()               
        
        # Sets the first set of coordinates to the min/max variables for easting, northing and elevation to initialize the variables
        min_easting = float(coord_line[0])      
        max_easting = float(coord_line[0])      

        min_northing = float(coord_line[1])
        max_northing = float(coord_line[1])

        min_elevation = float(coord_line[2])
        max_elevation = float(coord_line[2])

        # Loops through each line of coordinates
        for line in coordinates:

            # Splits each line so the values are seperate
            coord_line = line.split()
            
            # Loops through each seperate value in the line of coordinates
            for coord in coord_line:
                # If the min_easting in the new line is less than the original then replace min_easting wtih the lower value
                if float(coord_line[0]) < min_easting:      
                    min_easting = float(coord_line[0])      
                
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

        # Assigns line_count to the number of points property
        self.numPoints = line_count

        # Adds min_easting and min_northing to the lower-left coordinate list property
        self.LLcoord.append(min_easting)
        self.LLcoord.append(min_northing)
        # Converts the list for the lower-left coordinate to a tuple
        self.LLcoord = tuple(self.LLcoord)
        
        # Adds max_easting and the max_northing to the upper-right coordinate list property
        self.URcoord.append(max_easting)
        self.URcoord.append(max_northing)
        # Converts the list for the upper-right coordinate to a tuple
        self.URcoord = tuple(self.URcoord)

        # Assigns min_elevation to the minElev property
        self.minElev = min_elevation
        # Assigns max_elevation tot he maxElev property
        self.maxElev = max_elevation

        # Assigns tile_length to the width property
        self.width = tile_length
        # Assigns tile_height to the height property
        self.height = tile_height

        # Closes the file
        file.close()
    
    # Creates the method outputStatistics to print out the information to the user
    def outputStatistics(self):
        # Outputs the number of points
        print("Number of points: " + str(self.numPoints)) 

        # Outputs the lower-left coordinate
        print("Lower-left coordinate: UTM (6TM) " + str(self.LLcoord[0]) + " E " + str(self.LLcoord[1]) + " N")

        # Outputs the upper-right coordinate
        print("Upper-right coordinate: UTM (6TM) " + str(self.URcoord[0]) + " E " + str(self.URcoord[1]) + " N")    

        # Outputs the minimum elevation
        print("Minimum elevation: " + str(self.minElev) + " m")
        # Outputs the maximum elevation
        print("Maximum elevation: " + str(self.maxElev) + " m")

        # Outputs the tile size
        print("Tile size: " + str(self.width) + " km x " + str(self.height) + " km")


# Assigns the class to the file1 object
file1 = LiDAR15DEM()
# Asks the user for the file location for the file1 object
file1_location = str(input("What is the file location of the first file using forward slashes? \n(Must be a .xyz file ex. C:/LiDAR15/DEM.xyz): "))

print("File 1 info:")

# Opens and computes the statistics for the file1 object
file1.open(file1_location)
# Prints out the statistics computed by open() to the user
file1.outputStatistics()

# Assigns the class to the file2 object
file2 = LiDAR15DEM()
# Asks the user for the file location for the file2 object
file2_location = str(input("What is the file location of the second file using forward slashes? \n(Must be a .xyz file ex. C:/LiDAR15/DEM.xyz): "))

print("File 2 info: ")

# Opens and computes the statistics for the file2 object
file2.open(file2_location)
# Prints out the statistics computed by open() to the user
file2.outputStatistics()
