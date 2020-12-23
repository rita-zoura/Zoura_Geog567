# Rita Zoura | UCID: 30018933 | rita.zoura@ucalgary.ca
# Run using Python 3.6
# This script converts lat/long coordinates in Degrees, minutes, seconds (DMS)
# to lat/long coordinates in Decimal Degrees (DD)

# Tells the user the point of this tool and states some guidelines
print("Convert latitude/longitude coordinates from degrees, minutes, seconds, to decimal degrees.")
print("Do not inclue any apostrophe's or degrees symbols and enter each value seperately.")
print("Minutes and seconds should not have negative values. \n")

# Input the values for the latitudinal degrees, minutes and seconds seperately
lat_deg = int(input("Enter latitudinal degrees value: "))
lat_min = int(input("Enter latitudinal minutes value: "))
lat_sec = int(input("Enter latitudinal seconds value: "))

# Input the value for the longitudinal degrees, minutes, seconds seperately
long_deg = int(input("Enter longitudinal degrees value: "))
long_min = int(input("Enter longitudinal minutes value: "))
long_sec = int(input("Enter longitudinal seconds value: "))

# Convert latitudinal minutes to decimals
lat_dec_min = lat_min / 60
# Convert latitudinal seconds to decimals
lat_dec_sec = lat_sec / 3600

# Convert longitudinal minutes to decimals
long_dec_min = long_min / 60
# Convert longitudinal seconds to decimals
long_dec_sec = long_sec / 3600

# Add latitudinal decimal values to latitudinal degrees
if lat_deg < 0:                                     # if latitude degrees is negative then
    lat_deg = lat_deg * -1                          # removes the negative to ensure proper addition
    lat_dd = lat_deg + lat_dec_min + lat_dec_sec
    lat_dd = lat_dd * -1                            # adds the negative back to ensure proper coordinate direction
else:
    lat_dd = lat_deg + lat_dec_min + lat_dec_sec

# Add longitudinal decimal values to longitudinal degrees
if long_deg < 0:                                    # if longitude degrees is negative then
    long_deg = long_deg * -1                        # removes the negative to ensure proper addition
    long_dd = long_deg + long_dec_min + long_dec_sec
    long_dd = long_dd * -1                          # adds the negative back to ensure proper coordinate direction
else:
    long_dd = long_deg + long_dec_min + long_dec_sec

# Prints the output values to the user as a string value
print("Degrees latitude is " + str(lat_dd))
print("Degrees longitude is " + str(long_dd))
