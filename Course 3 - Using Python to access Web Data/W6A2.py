import urllib.request, urllib.parse, urllib.error
import json

serviceurl = "http://py4e-data.dr-chuck.net/geojson?"
address = input('Enter location: ')
if len(address) < 1 :
    address = "South Federal University"

#get the js page
print("Retrieving:", address)

url = serviceurl + urllib.parse.urlencode({'address': address})

rawjson = urllib.request.urlopen(url)
data = rawjson.read().decode()

#print the length of json
print("Retrieved", len(data), "characters")

try :
    js = json.loads(data)
except :
    js = None

if not js or 'status' not in js or js['status'] != 'OK':
    print("CANNOT RETRIEVE FILE")
    print(data)
else :
    #print(json.dumps(js, indent=4))
    print('Place id', js["results"][0]["place_id"])
