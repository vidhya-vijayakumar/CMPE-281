from geopy.geocoders import Nominatim
from geopy.distance import great_circle
geolocator = Nominatim()
# Function to locate the longitude and latitude of cities
def placelocator(place):
    location=geolocator.geocode(place)
    print(location.address)
    return(location.latitude,location.longitude)
#User Input
user_input_1=raw_input("Enter the first city: ")
place1=placelocator(user_input_1)
user_input_2=raw_input("Enter the second city: ")
place2=placelocator(user_input_2)
location1=geolocator.geocode("Coimbatore")
print "The distance between the two cities is "
print(great_circle(place1,place2).miles)
