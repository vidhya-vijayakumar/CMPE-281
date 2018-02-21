from geopy.geocoders import Nominatim
from geopy.distance import great_circle
geolocator = Nominatim()
#place1=raw_input("Enter the first city: ")
location1=geolocator.geocode("Coimbatore")
print(location1.address)
print(location1.latitude, location1.longitude)
#place2=raw_input("Enter the second city: ")
location2=geolocator.geocode("Trichy")
print(location2.address)
print(location2.latitude, location2.longitude)
a=(location1.latitude, location1.longitude)
b=(location2.latitude, location2.longitude)
print(great_circle(a,b).miles)
def text():
    x=1
    while x==1:
        print "hello"
