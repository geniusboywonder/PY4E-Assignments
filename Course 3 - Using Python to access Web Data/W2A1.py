import re

# get a file
name = input("Enter a file name: ")
if len(name) < 1 : name = "regex_sum_42.txt"

try:
    fh = open(name)
except:
    print("File cannot be found: ", name)
    quit()

Numlist = list()
numtot = float()


# run through each line in the file
for line in fh:
    line = line.rstrip()
    # find the stuff and extract all digits and . for floating points
    numlist = re.findall('[0-9]+', line)
    # check there is a value in stuff and add it to the list
    #if len(numlist) != 0 : continue
    for n in numlist :
        numtot = numtot + float(n)
print(numtot)
