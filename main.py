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
