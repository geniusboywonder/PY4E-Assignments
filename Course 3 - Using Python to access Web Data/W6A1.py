import urllib.request, urllib.parse, urllib.error
import json
import ssl

# Ignore SSL certificate errors
# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location: ')
if len(url) < 1 :
    url = "file:///C:/Users/neilla/OneDrive%20-%20Direct%20Axis/Neill/Python%20for%20Everybody/Git/PY4E-Assignments/Course%203%20-%20Using%20Python%20to%20access%20Web%20Data/comments_133480.json"

#get the js page
print("Retrieving:", url)
rawjson = urllib.request.urlopen(url)
data = rawjson.read().decode()

#print the length of xml
print("Retrieved", len(data), "characters")

try :
    js = json.loads(data)
except :
    js = None

if not js :
    print("CANNOT RETRIEVE FILE")
    print(data)
else :
    #print(json.dumps(js, indent=4))
    counts = 0
    print("Count:", len(js["comments"]))
    #sum the value of each count node
    for item in js["comments"] :
        counts = counts + item["count"]
    print('Sum:', counts)
