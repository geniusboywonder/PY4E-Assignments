import re

# get a file
name = input("Enter a file name: ")
if len(name) < 1 : name = "mbox-short.txt"

try:
    fh = open(name)
except:
    print("File cannot be found: ", name)
    quit()

Numlist = list()

# run through each line in the file
for line in fh:
    if len(line) < 3 or not line.startswith("From ") : continue
    line = line.rstrip()
    # find the stuff and extract all digits and . for floating points
    stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)', line)
    # check there is a value in stuff and add it to the list
    if len(stuff) != 1 : continue #only get 1 number or skip it
    num = float(stuff[0])
    numlist.append(num)
print("Max: ", max(numlist))
