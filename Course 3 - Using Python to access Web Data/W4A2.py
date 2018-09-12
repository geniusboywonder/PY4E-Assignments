import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
if len(url) < 1 :
    url = "http://py4e-data.dr-chuck.net/known_by_Fikret.html"
    pos = 3
    repeat = 4
else :
    pos = int(input('Enter Position: '))
    repeat = int(input('Enter Count: '))
start = 0
#get the first page
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

#repeat loop until counter = input repeat
while repeat > start :
    # Retrieve all of the a tags
    tags = soup('a')
    #get the next href based on input pos
    newurl = tags[pos-1].get('href', None)
    print('Retrieving:', newurl)
    #get the new html
    html = urllib.request.urlopen(newurl, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    start = start + 1
