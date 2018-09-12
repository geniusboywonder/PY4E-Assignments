import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
if len(url) < 1 : url = "http://py4e-data.dr-chuck.net/comments_42.html"
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

counts = float()

# Retrieve all of the td tags
tags = soup('span')

for tag in tags:
    #print(tag)
    counts = counts + float(re.findall('span class="comments">([0-9]+)', str(tag))[0])
print(counts)
