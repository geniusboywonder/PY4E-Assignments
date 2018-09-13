import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location: ')
if len(url) < 1 :
    url = "file:///C:/Users/neilla/OneDrive%20-%20Direct%20Axis/Neill/Python%20for%20Everybody/Git/PY4E-Assignments/Course%203%20-%20Using%20Python%20to%20access%20Web%20Data/comments_133479.xml"

#get the xml page
print("Retrieving:", url)
xml = urllib.request.urlopen(url, context=ctx).read()
#print the length of xml
print("Retrieved", len(xml), "characters")
tree = ET.fromstring(xml)
#find all the count nodes
comments = tree.findall('.//count')
counts = 0
#print the numbers of count nodes
print("Count:", len(comments))
#sum the value of each count node
for child in comments :
    counts = counts + int(child.text)
print('Sum:', counts)
