import phonenumbers

number = "+88 YOUR PHONE NUMBER"

from phonenumbers import geocoder
from phonenumbers import carrier
pepnumber = phonenumbers.parse(number)


location = geocoder.description_for_number(pepnumber, "en")
print("location ",location)
# service_pro = phonenumbers.parse(number)
service_pro = carrier.name_for_number(phonenumbers.parse(number), "en")


print("service pro", service_pro)


#=========================



from unittest import result
import phonenumbers
import folium
number = "YOUR PHONE NUMBER"

from phonenumbers import geocoder
from phonenumbers import carrier
pepnumber = phonenumbers.parse(number)


location = geocoder.description_for_number(pepnumber, "en")
print("location ",location)
# service_pro = phonenumbers.parse(number)
service_pro = carrier.name_for_number(phonenumbers.parse(number), "en")


print(f"service pro {number} - ", service_pro)


from opencage.geocoder import OpenCageGeocode
#https://opencagedata.com/
key = "YOUR API KEY"
geocoder = OpenCageGeocode(key)
# query = str(location)

results = geocoder.geocode(location)

print(results)

# lat = results[0]['geometry']['lat']
# lng = results[0]['geometry']['lng']


# myMap = folium.Map(location=[lat, lng], zoom_start=9)
# folium.Marker([lat, lng], popup=location).add_to(myMap)

# myMap.save("mylocation.html")
